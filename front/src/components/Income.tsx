import React, {useState} from 'react';
import {
    Text,
    Input,
    NumberDecrementStepper,
    NumberInput,
    NumberInputField,
    NumberInputStepper,
    NumberIncrementStepper,
    Box,
    IconButton,
    Flex,
    Spacer,
    Stat,
    StatNumber,
    Alert,
    AlertIcon,
    AlertTitle,
    AlertDescription,
} from '@chakra-ui/react'
import '../App.css';
import { FaEuroSign } from "react-icons/fa";
import {AddIcon, CheckIcon, Icon} from "@chakra-ui/icons";
import { Button, ButtonGroup } from '@chakra-ui/react'
import axios from 'axios';


export interface incomeItem {
    name: string,
    value: string,
    type: 'income' | 'expense'
}
interface IProps {
    title: string,
    placeholder: string,
    link: string

}
export default function Income (props: IProps) {



    const format = (val: string) => `€` + val
    const parse = (val: string) => val.replace(/^\$/, '')
    const [incomeValue, setIncomeValue] = React.useState('')
    const [jobValue, setJobValue] = React.useState('')
    const [incomeItems, setIncomeItem] = useState<incomeItem[]>([])
    const [validSubmit, setValidSubmit] = useState(true)
    const [dataSubmited, setDataSubmited] = useState(false)
    const [emptyName, setEmptyName] = useState(false)
    const [emptyValue, setEmptyValue] = useState(false)

    let totalIncome: number = 0
    incomeItems.forEach((item) => {

        totalIncome += Number(item.value)
    })

    let sendData = (): void => {
        let expenseItems = incomeItems.slice(0)
        axios.post(`http://127.0.0.1:8000/api/api/inc/`, props.link === 'inc' ? {incomeItems} : {expenseItems})
        .then(res => {
          console.log(res);
          console.log(res.data);
          setDataSubmited(true)
        })
    }

    return (
        <div className='Income'>
            <Flex>
                <Box>
                    <Text padding='0 0 10px 5px' fontSize='xl' >{props.title}</Text>
                </Box>
                <Spacer/>
                <Box>
                    <Stat>
                        <StatNumber>€{totalIncome}</StatNumber>
                    </Stat>
                </Box>
            </Flex>

            {incomeItems.map((item: incomeItem) => {
                return (
                        <Box padding='5px 20px' margin='10px' borderWidth='1px' borderRadius='lg'>
                            <Flex>
                            <Box
                                fontWeight='semibold'

                            >
                                {item.name}
                            </Box>
                            <Spacer/>
                            <Box className='p2'> € {item.value}</Box>
                            </Flex>

                        </Box>

                )
            })}
            {!dataSubmited ? 
            <div>


            <Box padding='20px' margin='10px' borderWidth='1px' borderRadius='lg'>

            <Input width='auto'
                onChange={(event) => {
                    if (event && event.target.value.length < 16) {
                        setJobValue(event.target.value)
                    }
                }}
                placeholder={props.placeholder}
                marginBottom='15px'
                isInvalid={true}
                value={jobValue} />
            <NumberInput step={10}
                         isRequired={true}
                         defaultValue={200}
                         min={10}
                         onChange={(valueString) => setIncomeValue(parse(valueString))}
                         value={format(incomeValue)}
            >
                <NumberInputField />
                <NumberInputStepper>
                    <NumberIncrementStepper />
                    <NumberDecrementStepper />
                </NumberInputStepper>
            </NumberInput>
        </Box>
        
        
            
            <Box>
            <ButtonGroup size='sm' isAttached variant='solid'>
            <Button 
                    colorScheme='green'
                    onClick={() => {
                        if (incomeItems.length !== 0) {
                            sendData();
                        } else {
                            setValidSubmit(false)
                        }
                    }}
                >
                    Submit
                </Button>
                  <IconButton 
                  colorScheme='green'
                    onClick={() => {
                        if (incomeValue.length > 0)
                        setValidSubmit(true)
                        const newIncomeItem: incomeItem = {
                            name: jobValue,
                            value: incomeValue,
                            type: props.link == 'inc' ? 'income' : 'expense'
                        }
                        setIncomeItem(incomeItems => [...incomeItems, newIncomeItem])
                    }}                  aria-label='Add to friends' icon={<AddIcon />} />
            </ButtonGroup>
                    {!validSubmit ? 
                        <Alert status='error' height='50px' margin='15px 0'>
                <AlertIcon />
                <AlertDescription>You have to add at least one {props.link === 'inc' ? 'income' : 'expense'}</AlertDescription>
              </Alert>  
                    
                  
                : ''}
            </Box>
            </div>
            : '' }
        </div>
    );
}

