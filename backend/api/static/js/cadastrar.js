async function enviarFormulario(evento){
    evento.preventDefault()
    
    const nome = document.getElementById("nome").value
    const senha = document.getElementById("senha").value
    const csrf = document.querySelector("[name=csrfmiddlewaretoken]").value

    const url = Window.location.href
    const valor = url.split("/")
    const id = valor[valor.length - 1]
    let resposta;
    
    if(id){

        resposta = await apiFetch(`/api/alunos/${id}`, "PUT", {nome: nome, senha: senha}, {"X-CSRFToken": csrf})
    }else{
        resposta = await apiFetch("/api/alunos", "POST", {nome: nome, senha: senha}, {"X-CSRFToken": csrf}) 
    }
    // const resposta = await apiFetch("/api/user", "POST", {nome: nome, senha: senha}, {"X-CSRFToken": csrf})
    

    if(resposta){
        window.location.href = "/home"
   

    }
}
var alunoForm = document.getElementById('alunoForm').addEventListener("submit", enviarFormulario)      