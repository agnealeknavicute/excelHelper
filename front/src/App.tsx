import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import Header from "./components/Header";
import { Box, Grid, Button, GridItem } from "@chakra-ui/react";
import Income from "./components/Income";
import axios from "axios";
import Expenses from "./components/Expenses";
import "bootstrap/dist/css/bootstrap.min.css";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/hello-world/")
      .then((response) => {
        setMessage(response.data.message);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  let getData = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/excelData/', {
          responseType: 'blob', // указываем, что ожидаем получить файловый объект (blob)
        });
    
        // Создаем ссылку для скачивания файла
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
    
        // Устанавливаем имя файла для скачивания
        link.setAttribute('download', 'example.xlsx');
    
        // Добавляем ссылку в документ и эмулируем клик по ней
        document.body.appendChild(link);
        link.click();
    
        // Очищаем ресурсы
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);
      } catch (error) {
        console.error('Ошибка при скачивании файла', error);
      }
  };
  return (
    <div className="App">
      <Container>
        <Row>
          <Header />
        </Row>
        <Row>
          <Col>
            <Box padding="15px" borderRadius="20px" borderWidth="1px">
              <Income link="inc" placeholder="Freelance" title="Your income" />
            </Box>
          </Col>
          <Col>
            <Box padding="15px" borderRadius="20px" borderWidth="1px">
              <Income link="exp" placeholder="Food" title="Your expences" />
            </Box>
          </Col>
          <Col xs={5}>
            <Button
              colorScheme="green"
              onClick={() => {
                getData();
              }}
            >
              Get excel file
            </Button>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
