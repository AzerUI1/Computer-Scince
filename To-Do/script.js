const input = document.getElementById('task-input');
const button = document.getElementById('add-btn');
const list = document.getElementById('task-list');
const emptyState = document.getElementById('empty-state');

function updateEmptyState() {
  if (list.children.length > 1) { // More than just the empty state
    emptyState.style.display = 'none';
  } else {
    emptyState.style.display = 'block';
  }
}

function createTaskElement(taskText) {
  const li = document.createElement('li');
  
  const taskSpan = document.createElement('span');
  taskSpan.className = 'task-text';
  taskSpan.textContent = taskText;
  
  const actionsDiv = document.createElement('div');
  actionsDiv.className = 'task-actions';
  
  const deleteBtn = document.createElement('button');
  deleteBtn.className = 'delete-btn';
  deleteBtn.innerHTML = '<i class="fas fa-trash"></i>';
  
  deleteBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    li.classList.add('fade-out');
    setTimeout(() => {
      li.remove();
      updateEmptyState();
    }, 300);
  });
  
  li.addEventListener('click', () => {
    li.classList.toggle('done');
  });
  
  actionsDiv.appendChild(deleteBtn);
  li.appendChild(taskSpan);
  li.appendChild(actionsDiv);
  
  return li;
}

button.addEventListener('click', () => {
  const taskText = input.value.trim();
  if(taskText === '') return;

  const li = createTaskElement(taskText);
  
  // Insert before empty state if it exists
  if (emptyState.style.display !== 'none') {
    list.insertBefore(li, emptyState);
  } else {
    list.appendChild(li);
  }
  
  input.value = '';
  updateEmptyState();
});

input.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    button.click();
  }
});

// Initial empty state check
updateEmptyState();
