import React, { useEffect } from 'react';
import { Api } from '../../../contexts/api';
import Transacao from './transacao';
import CadChavePix from './cad_chavePix';

import { Navbar, Form, InputGroup, Row, Col } from 'react-bootstrap';


const NavSaldoPessoaFIsica: React.FC = () => {

  const [saldo, setSaldo] = React.useState('');

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await Api.get('/usuarios/4/');
        // Acessar o saldo dentro de saldoUser
        const saldo = response.data.saldoUser[0]?.saldo || '0.00';
        setSaldo(saldo);
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    };

    fetchUserData();
  }, []);


    return (
        <Navbar className="bg-body-tertiary justify-content-between">
          <Form>
            <InputGroup>
              <InputGroup.Text id="basic-addon1">R$</InputGroup.Text>
              <Form.Control
                // disabled
                placeholder="Saldo"
                aria-describedby="basic-addon1"
                value={saldo}
              />
            </InputGroup>
          </Form>
          <Form>
            <Row>
            <Col xs="auto">
                <p>0000 / 00.000000.0</p>
              </Col>
              <Col xs="auto">
                <Transacao/>
              </Col>
              <Col xs="auto">
                <CadChavePix/>
              </Col>
            </Row>
          </Form>
        </Navbar>
      );
};

export default NavSaldoPessoaFIsica;