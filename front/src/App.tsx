import React, {useEffect, useState} from 'react';
import logo from './logo.svg';
import './App.css';
import Header from "./components/Header";
import {Box, Grid, Button, GridItem} from "@chakra-ui/react";
import Income from "./components/Income";
import axios from "axios";
import Expenses from "./components/Expenses";
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/hello-world/')
            .then(response => {
                setMessage(response.data.message);
            })
            .catch(error => {
                console.log(error);
            });
    }, []);
    let getData = (): void => {
        axios.get(`http://127.0.0.1:8000/api/api/excelData/`)
        .then(res => {
          console.log(res);
          console.log(res.data);
        })
    }
    return (
        <div className="App">

            <Container>
                <Row>
                    <Header/>
                </Row>
                <Row>
                    <Col>
                    <Box
                        padding='15px'
                        borderRadius='20px'
                        borderWidth='1px'>
                        <Income link='inc' placeholder='Freelance' title='Your income'/>
                    </Box>
                    </Col>
                    <Col>
                    <Box
                        padding='15px'
                        borderRadius='20px'
                        borderWidth='1px'>
                        <Income link='exp' placeholder='Food' title='Your expences'/>
                    </Box>
                    </Col>
                    <Col xs={5}>Visual</Col>
                </Row>
                <Row>
                    <Button 
                        onClick={() => {
                            getData()
                        }}
                    >
                        Submit
                    </Button>
                </Row>
            </Container>
        </div>
    );
}

export default App;
