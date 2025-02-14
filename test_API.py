import pytest
from fastapi.testclient import TestClient
from main import app  # Importe o seu app FastAPI

# Cria uma instância do TestClient para simular as requisições
client = TestClient(app)

# Testes para Empresas

# Testar criação de empresa
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

# Testar listagem de empresas
def test_listar_empresas():
    response = client.get("/empresas/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Espera que seja uma lista de empresas

# Testar obter uma empresa específica
def test_obter_empresa():
    # Primeiro, cria uma empresa
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000123", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]
    
    # Agora, tenta obter essa empresa
    response = client.get(f"/empresas/{empresa_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Empresa Teste"
    assert data["cnpj"] == "12345678000123"

# Testar atualizar uma empresa
def test_update_empresa():
    # Cria uma empresa
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000123", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]

    # Atualiza a empresa
    response = client.put(
        f"/empresas/{empresa_id}", 
        json={"nome": "Empresa Atualizada", "cnpj": "12345678000123", 
              "endereco": "Novo Endereço", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Empresa Atualizada"

# Testar deletar uma empresa
def test_delete_empresa():
    # Cria uma empresa
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000123", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]

    # Deleta a empresa
    response = client.delete(f"/empresas/{empresa_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Empresa Teste"

# Testes para Obrigações

# Testar criação de obrigação
def test_create_obrigacao():
    # Cria uma empresa
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000123", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]
    
    # Cria uma obrigação
    response = client.post(
        f"/empresas/{empresa_id}/obrigacoes/", 
        json={"descricao": "Obrigação Teste", "data_limite": "2025-12-31"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["descricao"] == "Obrigação Teste"
    assert data["empresa_id"] == empresa_id

# Testar listagem de obrigações
def test_listar_obrigacoes():
    # Cria uma empresa
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000123", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]

    # Cria obrigações
    client.post(
        f"/empresas/{empresa_id}/obrigacoes/", 
        json={"descricao": "Obrigação 1", "data_limite": "2025-12-31"}
    )
    client.post(
        f"/empresas/{empresa_id}/obrigacoes/", 
        json={"descricao": "Obrigação 2", "data_limite": "2025-12-31"}
    )
    
    # Lista as obrigações
    response = client.get(f"/empresas/{empresa_id}/obrigacoes/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

# Testar obter uma obrigação específica
def test_obter_obrigacao():
    # Cria uma empresa
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000123", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]
    
    # Cria uma obrigação
    response = client.post(
        f"/empresas/{empresa_id}/obrigacoes/", 
        json={"descricao": "Obrigação Teste", "data_limite": "2025-12-31"}
    )
    obrigacao_id = response.json()["id"]
    
    # Obtém a obrigação
    response = client.get(f"/obrigacoes/{obrigacao_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["descricao"] == "Obrigação Teste"

# Testar deletar uma obrigação
def test_delete_obrigacao():
    # Cria uma empresa
    response = client.post(
        "/empresa/", 
        json={"nome": "Empresa Teste", "cnpj": "12345678000123", 
              "endereco": "Endereço Teste", "email": "empresa@teste.com", "telefone": "1122334455"}
    )
    empresa_id = response.json()["id"]
    
    # Cria uma obrigação
    response = client.post(
        f"/empresas/{empresa_id}/obrigacoes/", 
        json={"descricao": "Obrigação Teste", "data_limite": "2025-12-31"}
    )
    obrigacao_id = response.json()["id"]
    
    # Deleta a obrigação
    response = client.delete(f"/obrigacoes/{obrigacao_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["descricao"] == "Obrigação Teste"