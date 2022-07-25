let open = document.querySelector('#open');

/* Aumanta para 270px a largura do box-modal */
open.addEventListener("click", () => {
  document.querySelector('.box-modal').style.width="270px";
})

/* Diminui para 0px o tamanho do box-modal */
document.querySelector('.close').addEventListener("click", () => {
  document.querySelector('.box-modal').style.width="0";
})