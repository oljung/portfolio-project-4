const showForm = (elementId) => {
    document.getElementById(elementId).classList.toggle('hide');
};

const itemStrikeout = (itemId) => {
    children = document.getElementById(`shopping-list-item-${itemId}`).children;
    for (let child of children) {
        child.style.textDecoration = "line-through";
    } 
};

const showIngredientForm = (name, unit) => {
    modal = document.getElementById('ingredient-form');
    modal.style.display = 'block';
    document.getElementById('ingredient-name').value = name;
    document.getElementById('ingredient-unit').value = unit;
};

const closeModalForm = (formId) => {
    document.getElementById(formId).style.display = 'none';
};

const showModalForm = (formId) => {
    document.getElementById(formId).style.display = 'block';
};

const goBack = () => window.history.back();