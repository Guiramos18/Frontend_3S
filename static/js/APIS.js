async function getGato() {
    let resultado = await fetch("https://api.thecatapi.com/v1/images/search")

    if (resultado.ok){
        let dados = await resultado.json()
        render_gato(dados)
    }
}

function render_gato(dados){
    let urlImg = dados[0].url
    const imgGato = document.getElementById("img-gato")
    const iconGato = document.getElementById("icon-gato")

    iconGato.style.display = "none"
    imgGato.style.display = "block"
    imgGato.src = urlImg
}


async function getCachorro() {
    let resultado = await fetch("https://api.thedogapi.com/v1/images/search")

    if (resultado.ok){
        let dados = await resultado.json()
        render_cachorro(dados)
    }
}

function render_cachorro(dados){
    let urlImg = dados[0].url
    const imgCachorro = document.getElementById("img-cachorro")
    const iconCachorro = document.getElementById("icon-cachorro")

    iconCachorro.style.display = "none"
    imgCachorro.style.display = "block"
    imgCachorro.src = urlImg
}


async function getRaposa() {
    let resultado = await fetch("https://api.thefoxapi.com/v1/images/search")

    if (resultado.ok){
        let dados = await resultado.json()
        render_raposa(dados)
    }
}

function render_raposa(dados){
    let urlImg = dados[0].url
    const imgRaposa = document.getElementById("img-raposa")
    const iconRaposa = document.getElementById("icon-raposa")

    iconRaposa.style.display = "none"
    imgRaposa.style.display = "block"
    imgRaposa.src = urlImg
}