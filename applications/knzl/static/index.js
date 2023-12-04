import {testModulo} from "./main.js";


let savedScripts;
let openScript;

let results = document.getElementById("results")
let form = document.querySelector('form');
let editor = document.getElementById("editor");
let buttonSave = document.getElementById("button-save")
let buttonOpen = document.getElementById("button-open")
let buttonClear = document.getElementById("button-clear")

document.addEventListener("DOMContentLoaded",(event)=>{
      savedScripts = localStorage
      if(openScript){
        results.innerHTML = ""
      }
})

editor.addEventListener("keydown", function(event) {
  if (event.key === "Tab") {
    event.preventDefault(); 
    let start = this.selectionStart;
    console.log("Start",start)
    let end = this.selectionEnd;
    console.log("End",end)
    this.value = this.value.substring(0, start) + "\t" + this.value.substring(end);
    console.log("Value",this.value)
    this.selectionStart = this.selectionEnd = start + 1;
    console.log("SS",this,this.selectionStart)
  }
});

/** Boton para salvar el Script  */
buttonSave.addEventListener("click",(e)=>{
  if(openScript){
    localStorage.setItem(openScript, encodeURIComponent(editor.value))
  }else{
    console.log("Saving Script")
    Swal.fire({
      title: 'Script Name',
      input: 'text',
      inputAttributes: {
        autocapitalize: 'off'
      },
      showCancelButton: true,
      confirmButtonText: 'Save',
      allowOutsideClick: () => !Swal.isLoading()
    }).then((result) => {
      if (result.isConfirmed) {
        const name = `${result.value}`
        localStorage.setItem(`${name}`, encodeURIComponent(editor.value))
        savedScripts = localStorage
      }
    })
  }  
})

buttonOpen.addEventListener("click",(e)=>{
    console.log("Open Script")
    console.log(savedScripts)
    if(savedScripts.length > 0){
      const code = localStorage.getItem('knzl-test')
      editor.value= decodeURIComponent(code)
      openScript = 'knzl-test'
    }
    
})

form.addEventListener('submit', function() {
    results.innerText = "";
    let loader = document.getElementById('loader');
    loader.style.display = 'block';  
});

buttonClear.addEventListener('click', function() {
  results.innerText = "";
  });



