import React, {useEffect, useState} from 'react';
import logo from './logo.svg';
import './App.css';
import Header from "./components/Header";
import {Grid, GridItem} from "@chakra-ui/react";
import Income from "./components/Income";
import axios from "axios";

function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/hello-world/')
            .then(response => {
                debugger
                setMessage(response.data.message);
            })
            .catch(error => {
                console.log(error);
            });
    }, []);
  return (
    <div className="App">
        {message}
        <Grid
            templateAreas={`"header header"
                  "nav main"
                  "nav main"`}
            gridTemplateColumns={'auto 1fr'}
            h='200px'
            gap='1'

        >
            <GridItem pl='2'area={'header'}>
                <Header />
            </GridItem>
            <GridItem pl='2'  area={'nav'}>
                <Income/>
            </GridItem>
            <GridItem pl='2' bg='green.300' area={'main'}>
                Main
            </GridItem>
        </Grid>
    </div>
  );
}

export default App;
