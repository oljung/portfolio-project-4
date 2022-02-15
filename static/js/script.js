

const showForm = (elementId) => {
    document.getElementById(elementId).classList.toggle('hide');
};

function itemStrikeout(itemId) {
    children = document.getElementById(`shopping-list-item-${itemId}`).children;
    for (let child of children) {
        child.style.textDecoration = "line-through";
    } 
}

function showIngredientForm(name, unit) {
    modal = document.getElementById('ingredient-form');
    modal.style.display = 'block';
    document.getElementById('ingredient-name').value = name;
    document.getElementById('ingredient-unit').value = unit;
}

function closeModalForm(formId) {
    document.getElementById(formId).style.display = 'none';
}

function showModalForm(formId) {
    document.getElementById(formId).style.display = 'block';
}