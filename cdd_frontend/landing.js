


window.addEventListener('DOMContentLoaded', () => {
  const hash = window.location.hash.substring(1);
  if (hash) {
    try {
      const decoded = decodeURIComponent(hash);
      const parsed = JSON.parse(decoded);
      renderCytoscape(parsed);
      return;
    } catch (err) {
      console.error("Failed to load JSON from URL fragment:", err);
    }
  }
});


// Example JSON schema.
// In a real application you might fetch this from your backend:
// fetch('/path/to/schema.json').then(response => response.json()).then(schema => { ... });

fetch('data.json')
  .then(response => response.json())
  .then(data => {

    renderCytoscape(data);

  })
  .catch(error => console.error('Error loading JSON:', error));



function renderCytoscape(openDIJson) {
    
// Example JSON schema.
// In a real application you might fetch this from your backend:
// fetch('/path/to/schema.json').then(response => response.json()).then(schema => { ... });

fetch('data.json')
  .then(response => response.json())
  .then(data => {

    renderCytoscape(data);

  })
  .catch(error => console.error('Error loading JSON:', error));



function renderCytoscape(openDIJson) {

  const diagram = openDIJson.diagrams[0]; // Assume first diagram
  const elements = [];

  // Process nodes
  const nodeMap = {};
  diagram.elements.forEach(element => {
    const nodeId = element.meta.uuid;
    const nodeName = element.meta.name;
    const nodeType = element.causalType;
    const nodeLabel = `${nodeName} \n______________\n\n${nodeType}`;
    const position = element.content.position || { x: 0, y: 0 };

    const node = {
      data: { id: nodeId, label: nodeLabel },
      position
    };

    elements.push(node);
    nodeMap[nodeId] = nodeLabel;
  });

  // Process edges
  diagram.dependencies.forEach(dep => {
    elements.push({
      data: {
        id: dep.meta.uuid,
        source: dep.source,
        target: dep.target,
        label: dep.meta.name || nodeMap[dep.source] + " → " + nodeMap[dep.target]
      }
    });
  });

  // Initialize Cytoscape
  const cy = cytoscape({
    container: document.getElementById('cy'),
    elements: elements,
    style: [
      {
        selector: 'node',
        style: {
          'background-color': '#46aeb8',
          'label': 'data(label)',
          'color': '#fff',
          'text-valign': 'center',
          'width': 110,
          'height': 40,
          'font-size': '14px',
          'shape': 'round-rectangle',
          'text-wrap': 'wrap',
          'text-max-width': 100,
          'padding': 25,
          'font-family': 'Sans-serif'
        }
      },
      {
        selector: 'edge',
        style: {
          'width': 3,
          'line-color': '#ccc',
          'target-arrow-color': '#ccc',
          'target-arrow-shape': 'triangle',
          'curve-style': 'bezier',
          'font-size': '10px',
          'text-rotation': 'autorotate',
          'text-margin-y': -10
        }
      }
    ],
    layout: {
      name: 'preset',
      // Override the positions function to scale up the existing coords
      // positions: function (node) {
      //   const p = node.position(); 
      //   // Example: double the x/y to increase spacing
      //   return { x: p.x, y: p.y * 2 };
      // },
      fit: true,
      padding: 30,
      animate: true,
      animationEasing: 'ease-out',
      animationDuration: 1000
    },
    
    wheelSensitivity: 0.5

  });
      
  // Enable right-click editing of node labels
  cy.on('tap', 'node', function(evt) {
    const node = evt.target;
    const newLabel = prompt("Edit node label:", node.data('label'));
    if (newLabel !== null && newLabel.trim() !== "") {
        node.data('label', newLabel);
    }
    });


  }
    

}
    
