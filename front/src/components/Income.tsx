import React, {useState} from 'react';
import {
    Text,
    Input,
    NumberDecrementStepper,
    NumberInput,
    NumberInputField,
    NumberInputStepper,
    NumberIncrementStepper,
    InputLeftElement,
    InputGroup,
    Box,
    IconButton,
    Flex,
    Spacer,
    StatHelpText,
    Stat,
    StatLabel,
    StatNumber
} from '@chakra-ui/react'
import '../App.css';
import { FaEuroSign } from "react-icons/fa";
import {AddIcon, CheckIcon, Icon} from "@chakra-ui/icons";

export interface incomeItem {
    name: string,
    income: string
}
export default function Income () {



    const format = (val: string) => `€` + val
    const parse = (val: string) => val.replace(/^\$/, '')
    const [incomeValue, setIncomeValue] = React.useState('300.00')
    const [jobValue, setJobValue] = React.useState('Job')
    const [incomeItems, setIncomeItem] = useState<incomeItem[]>([{
        name: jobValue,
        income: incomeValue
    }])

    return (
        <div className='Income'>
            <Flex>
                <Box>
                    <Text padding='0 0 10px 5px' fontSize='xl' >Your income</Text>
                </Box>
                <Spacer/>
                <Box>
                    <Stat>
                        <StatNumber>€0.00</StatNumber>
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

                <Input
                    onChange={(event) => {
                        if (event) {
                            setJobValue(event.target.value)
                        }
                    }}

                    marginBottom='15px'
                    value={jobValue} />
                <NumberInput precision={2} step={10}
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
                {/*<IconButton*/}
                {/*    isRound={true}*/}
                {/*    variant='solid'*/}
                {/*    colorScheme='blue'*/}
                {/*    aria-label='Done'*/}
                {/*    fontSize='20px'*/}
                {/*    icon={<CheckIcon />}*/}
                {/*/>*/}
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

        </div>
    );
}

