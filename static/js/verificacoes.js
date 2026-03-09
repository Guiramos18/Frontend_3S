//var nome = prompt("Como você chama?")

// "Nome" igual a ''
// if (nome == null) {
//     alert("Recarregue a página")
// } else {
//     let correto = confirm("Você se chama " + nome + "?")
//
//     if (correto) {
//         alert(nome + " Bem vindo ao site de cursos")
//     } else {
//         alert("Recarregue a página")
//     }
// }

function limpaInputsLogin() {
    const inputEmail = document.getElementById('input-email')
    const inputSenha = document.getElementById('input-senha')

    inputEmail.value = ''
    inputSenha.value = ''
}

function limpaInputsCadastro() {
    const inputNome = document.getElementById('input-nome')
    const inputDataNasc = document.getElementById('input-data-nasc')
    const inputCpf = document.getElementById('input-cpf')
    const inputEmail = document.getElementById('input-email2')
    const inputSenha = document.getElementById('input-senha2')
    const inputCargo = document.getElementById('input-cargo')
    const inputSalario = document.getElementById('input-salario')

    inputNome.value = ''
    inputDataNasc.value = ''
    inputCpf.value = ''
    inputEmail.value = ''
    inputSenha.value = ''
    inputCargo.value = ''
    inputSalario.value = ''
}

document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById('form-login')

    formLogin.addEventListener("submit", function (event) {
        const inputEmail = document.getElementById('input-email')
        const inputSenha = document.getElementById('input-senha')

        let temErro = false

        // Verificar se os inputs estão vazios

        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }


        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

    })

    const formCadastro = document.getElementById('form-cadastro')

    formCadastro.addEventListener("submit", function (event) {
        const inputNome = document.getElementById('input-nome')
        const inputDataNasc = document.getElementById('input-data-nasc')
        const inputCpf = document.getElementById('input-cpf')
        const inputEmail = document.getElementById('input-email2')
        const inputSenha = document.getElementById('input-senha2')
        const inputCargo = document.getElementById('input-cargo')
        const inputSalario = document.getElementById('input-salario')

        let temErro = false

        // Verificar se os inputs estão vazios

        if (inputNome.value === '') {
            inputNome.classList.add('is-invalid')
            temErro = true
        } else {
            inputNome.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }


        if (inputDataNasc.value === '') {
            inputDataNasc.classList.add('is-invalid')
            temErro = true
        } else {
            inputDataNasc.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

        if (inputCpf.value === '') {
            inputCpf.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

        if (inputCargo.value === '') {
            inputCargo.classList.add('is-invalid')
            temErro = true
        } else {
            inputCargo.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

        if (inputSalario.value === '') {
            inputSalario.classList.add('is-invalid')
            temErro = true
        } else {
            inputSalario.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

    })

})

