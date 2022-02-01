

const showForm = (elementId) => {
    document.getElementById(elementId).classList.toggle('hide');
};

function itemStrikeout(itemId) {
    children = document.getElementById(`shopping-list-item-${itemId}`).children;
    for (let child of children) {
        child.style.textDecoration = "line-through";
    } 
}