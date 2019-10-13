const titleinput = document.querySelector('input[name=title]');
const sluginput = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g,'-and-') //replace & with '-and-'
        .replace(/[\s\W-]+/g,'-') //replace spaces, non word chars and dashes with a single dash
};

titleinput.addEventListener('keyup',(e)=>{
    sluginput.setAttribute('value',slugify(titleinput.value));
});