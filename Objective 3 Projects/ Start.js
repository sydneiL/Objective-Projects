
const button = document.getElementById('Start')

// Disable the selected button in JavaScript based on a condition
// If the button text is 'Can you click me?'
if (button.innerText === 'Can you click me?') {
  button.disabled = true
}

// If you want to enable the button using JavaScript
      // you can switch back the `disabled` property to `false`
      // button.disabled = false
