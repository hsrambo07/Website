
const app = document.getElementById('root')


const container = document.createElement('div')
container.setAttribute('class', 'container')

var request = new XMLHttpRequest()

request.open('GET','https://thevirustracker.com/free-api?global=stats',true)

request.onload=function(){

    var data= JSON.parse(this.response)


    if(request.status>=200 && request.status <400){
        Object.keys(data).forEach(result=>{



            const card = document.createElement('div')
            card.setAttribute('class', 'card')


            const h1 = document.createElement('h1')
            h1.textContent =result.results.total_cases
            h1.setAttribute('class','count')
    
      
            container.appendChild(card)
            card.appendChild(h1)
            
          })
    }

    else{
        
        const errorMessage = document.createElement('marquee')
    errorMessage.textContent = `Gah, it's not working!`
    app.appendChild(errorMessage)
  }
}


request.send()


