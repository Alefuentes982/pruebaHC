
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')

const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

 
 const dropdownToggle = document.getElementById('dropdownMenuButton');

 const dropdownMenu = document.getElementById('dropdown-menu');


 dropdownToggle.addEventListener('mouseenter', function() {
     dropdownMenu.classList.add('show');
 });

 
 dropdownMenu.addEventListener('mouseleave', function() {
     dropdownMenu.classList.remove('show');
 });