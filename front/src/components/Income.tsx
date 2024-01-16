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
    StatNumber
} from '@chakra-ui/react'
import '../App.css';
import { FaEuroSign } from "react-icons/fa";
import {AddIcon, CheckIcon, Icon} from "@chakra-ui/icons";
import { Button, ButtonGroup } from '@chakra-ui/react'
import axios from 'axios';


export interface incomeItem {
    name: string,
    income: string
}
interface IProps {
    title: string,
    placeholder: string,

}
export default function Income (props: IProps) {



    const format = (val: string) => `€` + val
    const parse = (val: string) => val.replace(/^\$/, '')
    const [incomeValue, setIncomeValue] = React.useState('')
    const [jobValue, setJobValue] = React.useState('')
    const [incomeItems, setIncomeItem] = useState<incomeItem[]>([])
    let totalIncome: number = 0
    incomeItems.forEach((item) => {

        totalIncome += Number(item.income)
    })

    let sendData = (): void => {
        axios.post(`http://127.0.0.1:8000/api/api/inc/`, {incomeItems})
        .then(res => {
          console.log(res);
          console.log(res.data);
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
                            <Box className='p2'> € {item.income}</Box>
                            </Flex>

                        </Box>

                )
            })}
            <Box padding='20px' margin='10px' borderWidth='1px' borderRadius='lg'>

                <Input width='auto'
                    onChange={(event) => {
                        if (event && event.target.value.length < 16) {
                            setJobValue(event.target.value)
                        }
                    }}
                    placeholder={props.placeholder}
                    marginBottom='15px'
                    value={jobValue} />
                <NumberInput step={10}
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

            <div className='iconAddSec'>
                <IconButton
                    isRound={true}
                    variant='solid'
                    colorScheme='blue'
                    aria-label='Done'
                    fontSize='20px'
                    icon={<AddIcon />}
                    onClick={() => {
                        const newIncomeItem: incomeItem = {
                            name: jobValue,
                            income: incomeValue
                        }
                        setIncomeItem(incomeItems => [...incomeItems, newIncomeItem])
                    }}
                />
            </div>
            <Box>
                <Button 
                    onClick={sendData}
                >
                    Submit
                </Button>
            </Box>
        </div>
    );
}

