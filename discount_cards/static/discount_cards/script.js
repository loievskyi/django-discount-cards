let container = null;

document.addEventListener('DOMContentLoaded', () => {
    container = document.querySelector('.table');
    container.addEventListener('click', OnDeleteItemHandler);
})

function deleteRequest(url, parent) {
    fetch(url, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.status === 204) {
          parent.remove();
        }
        else {
          alert("Удалить не удалось :(");
        }
    })
    .catch(error => {
      alert("Удалить не удалось :(");
      console.error('Удалить не удалось :(', error);
    });
}

function OnDeleteItemHandler({ target} ) {
    if (target.classList.contains('delete-btn')) {
        let deleteUrl = target.getAttribute('data-delete-url');
        const parent = target.closest('[data-row]');
        if(parent) {
          if (confirm(`Удалить карту ${target.getAttribute('data-name')}?`)) {
            deleteRequest(deleteUrl, parent);
          }
        }
    }
}
