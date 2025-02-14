import pytest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

# Testes para Empresas

def test_create_empresa():
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000123", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Empresa Teste"
    assert data["cnpj"] == "12345678000123"

def test_listar_empresas():
    response = client.get("/empresas/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_obter_empresa():
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000124", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]
    
    response = client.get(f"/empresas/{empresa_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Empresa Teste"
    assert data["cnpj"] == "12345678000124"

def test_update_empresa():
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000125", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]

    response = client.put(
        f"/empresas/{empresa_id}", 
        json={"nome": "Empresa Atualizada", "cnpj": "12345678000125", 
              "endereco": "Novo Endereço", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Empresa Atualizada"

def test_delete_empresa():
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000126", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]

    response = client.delete(f"/empresas/{empresa_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Empresa Teste"



# Testes para Obrigações

def test_create_obrigacao():
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000127", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]
    
    response = client.post(
        f"/empresas/{empresa_id}/obrigacoes/", 
        json={"nome": "Obrigação Teste", "periodicidade": "Mensal"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Obrigação Teste"
    assert data["empresa_id"] == empresa_id

def test_listar_obrigacoes():
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000128", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]

    client.post(
        f"/empresas/{empresa_id}/obrigacoes/", 
        json={"nome": "Obrigação 1", "periodicidade": "Mensal"}
    )
    client.post(
        f"/empresas/{empresa_id}/obrigacoes/", 
        json={"nome": "Obrigação 2", "periodicidade": "Mensal"}
    )
    
    response = client.get(f"/empresas/{empresa_id}/obrigacoes/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

def test_obter_obrigacao():
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000129", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]
    
    response = client.post(
        f"/empresas/{empresa_id}/obrigacoes/", 
        json={"nome": "Obrigação Teste", "periodicidade": "Mensal"}
    )
    obrigacao_id = response.json()["id"]
    
    response = client.get(f"/obrigacoes/{obrigacao_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Obrigação Teste"

def test_delete_obrigacao():
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000130", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]
    
    response = client.post(
        f"/empresas/{empresa_id}/obrigacoes/", 
        json={"nome": "Obrigação Teste", "periodicidade": "Mensal"}
    )
    obrigacao_id = response.json()["id"]
    
    response = client.delete(f"/obrigacoes/{obrigacao_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Obrigação Teste"

def test_update_obrigacao():
    # Criar uma empresa
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000131", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]

    response = client.post(
        f"/empresas/{empresa_id}/obrigacoes/", 
        json={"nome": "Obrigação Teste", "periodicidade": "Mensal"}
    )
    obrigacao_id = response.json()["id"]
    
    response = client.put(
        f"/obrigacoes/{obrigacao_id}",
        json={"nome": "Obrigação Teste Alterada", "periodicidade": "Anual"}
    )
    
    assert response.status_code == 200
    
    data = response.json()
    assert data["nome"] == "Obrigação Teste Alterada"
    assert data["periodicidade"] == "Anual"
