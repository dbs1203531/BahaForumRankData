function buildIframeCode(src, width, height) {
  return [
    "<iframe",
    `  src="${src}"`,
    `  width="${width}"`,
    `  height="${height}"`,
    '  style="border:0;"',
    '  loading="lazy">',
    "</iframe>",
  ].join("\n");
}

async function copyText(text, button) {
  try {
    await navigator.clipboard.writeText(text);
    const original = button.textContent;
    button.textContent = "已複製";
    window.setTimeout(() => {
      button.textContent = original;
    }, 1600);
  } catch (error) {
    console.error("Failed to copy iframe code", error);
  }
}

function hydrateExample(card) {
  const relativeSrc = card.dataset.embedSrc;
  const width = card.dataset.embedWidth || "100%";
  const height = card.dataset.embedHeight || "480";
  const absoluteSrc = new URL(relativeSrc, window.location.href).toString();
  const iframe = card.querySelector(".demo-frame");
  const codeBlock = card.querySelector(".embed-code");
  const copyButton = card.querySelector(".copy-button");
  const frameShell = card.querySelector(".frame-shell");
  const markup = buildIframeCode(absoluteSrc, width, height);

  iframe.src = relativeSrc;
  iframe.width = width;
  iframe.height = height;

  if (frameShell && width !== "100%") {
    frameShell.style.maxWidth = `${width}px`;
  }

  if (codeBlock) {
    codeBlock.textContent = markup;
  }

  if (copyButton) {
    copyButton.addEventListener("click", () => copyText(markup, copyButton));
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-embed-src]").forEach(hydrateExample);
});
