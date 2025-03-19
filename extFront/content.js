// content.js
const REPO_URL_PATTERN = /^https:\/\/github\.com\/[^/]+\/[^/]+/;
let cloneOption = 'simple'; // 'simple' or 'explain'

// Create clone button
function createCloneButton() {
  const btn = document.createElement('button');
  btn.id = 'GH_CLONE_BUTTON';
  btn.innerHTML = `
    <span style="display: flex; align-items: center; gap: 6px">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
        <path fill="#ffffff" d="M5 3h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm0 2v14h14V5H5zm2 2h10v4h-2V9H9v2h2v2H7V7zm4 4v2h2v-2h-2zm-4 4v2h10v-2H7z"/>
      </svg>
      Clone
    </span>
  `;

  Object.assign(btn.style, {
    background: '#2ea44f',
    color: 'white',
    padding: '6px 16px',
    borderRadius: '6px',
    border: '1px solid rgba(27,31,35,.15)',
    cursor: 'pointer',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
    fontWeight: '600',
    boxShadow: '0 1px 3px rgba(0,0,0,0.1)',
    display: 'flex',
    alignItems: 'center',
    marginLeft: '8px',
    transition: 'filter 0.2s'
  });

  btn.addEventListener('mouseenter', () => btn.style.filter = 'brightness(1.1)');
  btn.addEventListener('mouseleave', () => btn.style.filter = 'none');

  return btn;
}

// Create clone option element with selection indicator
function createCloneOption(title, description, isSelected, value) {
  const option = document.createElement('div');
  option.style.cssText = `
    flex: 1;
    padding: 12px;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
    background-color: ${isSelected ? '#f0fdf4' : '#fff'};
    border-color: ${isSelected ? '#16a34a' : '#e5e7eb'};
    margin: 4px;
  `;
  
  option.dataset.value = value;

  option.onclick = () => {
    cloneOption = value;
    document.querySelectorAll('.clone-option').forEach(opt => {
      const dot = opt.querySelector('.option-dot');
      if (opt.dataset.value === cloneOption) {
        opt.style.backgroundColor = '#f0fdf4';
        opt.style.borderColor = '#16a34a';
        if (dot) dot.style.backgroundColor = '#16a34a'; // Green for selected
      } else {
        opt.style.backgroundColor = '#fff';
        opt.style.borderColor = '#e5e7eb';
        if (dot) dot.style.backgroundColor = '#e5e7eb'; // Gray for unselected
      }
    });
  };

  const dot = document.createElement('div');
  dot.style.cssText = `
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background-color: ${isSelected ? '#16a34a' : '#e5e7eb'};
    margin-right: 8px;
  `;
  dot.className = 'option-dot';

  const textContainer = document.createElement('div');
  const titleElem = document.createElement('div');
  titleElem.style.cssText = `
    font-weight: 500;
    font-size: 14px;
    color: #1f2937;
    margin-bottom: 2px;
  `;
  titleElem.textContent = title;

  const descElem = document.createElement('div');
  descElem.style.cssText = `
    font-size: 12px;
    color: #6b7280;
  `;
  descElem.textContent = description;

  const flexContainer = document.createElement('div');
  flexContainer.style.display = 'flex';
  flexContainer.style.alignItems = 'center';
  flexContainer.appendChild(dot);
  flexContainer.appendChild(titleElem);

  textContainer.appendChild(flexContainer);
  textContainer.appendChild(descElem);
  option.appendChild(textContainer);

  option.className = 'clone-option';
  return option;
}

// Show modal dialog for path input with validation
function showPathDialog() {
  cloneOption = 'simple'; // Reset to default option

  const modal = document.createElement('div');
  modal.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10000;
  `;

  const dialog = document.createElement('div');
  dialog.style.cssText = `
    background: white;
    padding: 20px;
    border-radius: 12px;
    width: 440px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
  `;

  // Header
  const header = document.createElement('h3');
  header.textContent = 'Clone Repository';
  header.style.cssText = `
    font-size: 18px;
    font-weight: 600;
    color: #1f2937;
    margin-bottom: 20px;
  `;

  // Options container
  const optionsContainer = document.createElement('div');
  optionsContainer.style.cssText = `
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
  `;

  // Create options
  const simpleOption = createCloneOption(
    'Simple Clone',
    'Just clone the repository',
    true,
    'simple'
  );
  const explainOption = createCloneOption(
    'With Notes',
    'Clone with explanation',
    false,
    'explain'
  );
  optionsContainer.append(simpleOption, explainOption);

  // Path input
  const inputContainer = document.createElement('div');
  inputContainer.style.marginBottom = '20px';
  
  const label = document.createElement('label');
  label.textContent = 'Destination Path';
  label.style.cssText = `
    display: block;
    font-size: 14px;
    color: #374151;
    margin-bottom: 8px;
  `;

  const input = document.createElement('input');
  input.placeholder = '/projects/my-repo';
  input.style.cssText = `
    width: 100%;
    padding: 8px 12px;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    font-size: 14px;
    outline: none;
    transition: border-color 0.2s;
  `;
  input.addEventListener('focus', () => {
    input.style.borderColor = '#16a34a';
    input.style.boxShadow = '0 0 0 2px rgba(22, 163, 74, 0.1)';
  });
  input.addEventListener('blur', () => {
    input.style.borderColor = '#d1d5db';
    input.style.boxShadow = 'none';
  });

  // Error message for invalid path
  const errorMessage = document.createElement('div');
  errorMessage.style.cssText = `
    color: #dc2626;
    font-size: 12px;
    margin-top: 4px;
    display: none;
  `;

  inputContainer.append(label, input, errorMessage);

  // Footer buttons
  const footer = document.createElement('div');
  footer.style.cssText = `
    display: flex;
    justify-content: flex-end;
    gap: 12px;
    padding-top: 20px;
    border-top: 1px solid #f3f4f6;
  `;

  const cancelBtn = document.createElement('button');
  cancelBtn.textContent = 'Cancel';
  cancelBtn.style.cssText = `
    padding: 8px 16px;
    background: #fff;
    border: 1px solid #d1d5db;
    color: #374151;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s;
  `;
  cancelBtn.onmouseenter = () => {
    cancelBtn.style.backgroundColor = '#f3f4f6';
  };
  cancelBtn.onmouseleave = () => {
    cancelBtn.style.backgroundColor = '#fff';
  };

  const confirmBtn = document.createElement('button');
  confirmBtn.textContent = 'Clone Repository';
  confirmBtn.style.cssText = `
    padding: 8px 16px;
    background: #16a34a;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.2s;
  `;
  confirmBtn.onmouseenter = () => {
    confirmBtn.style.backgroundColor = '#15803d';
  };
  confirmBtn.onmouseleave = () => {
    confirmBtn.style.backgroundColor = '#16a34a';
  };

  // Event handlers
  const removeModal = () => {
    document.body.removeChild(modal);
    document.body.style.overflow = 'auto';
  };

  cancelBtn.onclick = removeModal;
  confirmBtn.onclick = () => {
    const path = input.value.trim();
    if (!path) {
      errorMessage.textContent = 'Path cannot be empty.';
      errorMessage.style.display = 'block';
      return;
    }
    const invalidChars = /[<>"|?*]/;
    if (invalidChars.test(path)) {
      errorMessage.textContent = 'Path contains invalid characters.';
      errorMessage.style.display = 'block';
      return;
    }
    errorMessage.style.display = 'none';
    const withExplanation = cloneOption === 'explain';


  // Sends a POST request to http://127.0.0.1:8000/clone.
  //Passes the URL, destination path, and explanation choice in the body.
  //Alerts the user about success/failure.

  fetch("http://127.0.0.1:8000/clone", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    url: window.location.href.replace(/\/$/, "") + ".git",
    path: path,
    explain: withExplanation,
  }),
})
  .then((response) => {
    if (!response.ok) {
      return response.json().then((data) => {
        throw new Error(data.detail || "Error cloning repository");
      });
    }
    return response.json();
  })
  .then((data) => {
    alert(
      `Clone successful!\nExplanation was ${
        data.explanation ? "enabled" : "disabled"
      }.`
    );
  })
  .catch((err) => {
    alert("Failed to clone: " + err.message);
  });

    removeModal();
  };

  footer.append(cancelBtn, confirmBtn);
  dialog.append(header, optionsContainer, inputContainer, footer);
  modal.appendChild(dialog);

  document.body.style.overflow = 'hidden';
  document.body.appendChild(modal);
  input.focus();
}

// Main handler
function handleClone() {
  showPathDialog();
}

// Button integration
function initializeButton() {
  if (!REPO_URL_PATTERN.test(window.location.href)) return;

  const container = document.querySelector([
    '.file-navigation', 
    '[data-testid="repository-actions"]',
    '.Layout-sidebar'
  ].join(','));

  if (container && !document.getElementById('GH_CLONE_BUTTON')) {
    const btn = createCloneButton();
    btn.addEventListener('click', handleClone);
    container.prepend(btn);
  }
}

// MutationObserver for dynamic content
const observer = new MutationObserver(initializeButton);
observer.observe(document.body, {
  childList: true,
  subtree: true
});

// Initial setup
initializeButton();

// Handle GitHub's navigation
document.addEventListener('pjax:end', initializeButton);