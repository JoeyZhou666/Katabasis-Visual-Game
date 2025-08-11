import React, { useEffect, useRef, useState } from 'react';
import cytoscape from 'cytoscape';

interface SimpleCytoscapeGraphProps {
  onNodeSelect?: (label: string) => void;
}

// Initial data
const initialData = {
  nodes: [
    { id: 'disruptive_scenario', label: 'Bandit distracts you in class\n______________\n\nLever', position: { x: 350, y: 100 } },
    { id: 'brief_response', label: 'Ignore him\n______________\n\nIntermediate', position: { x: 600, y: 100 } },
    { id: 'focus_on_lesson', label: 'Teacher gives warning\n______________\n\nOutcome', position: { x: 850, y: 50 } },
  ],
  edges: [
    { id: 'edge18', source: 'disruptive_scenario', target: 'brief_response', label: 'Look down and focus on the lesson' },
    { id: 'edge19', source: 'brief_response', target: 'focus_on_lesson', label: 'Teacher notices' },
  ]
};

// Custom edit modal component
interface EditModalProps {
  isOpen: boolean;
  title: string;
  initialValue: string;
  onClose: () => void;
  onSave: (value: string) => void;
}

// Custom confirmation modal component
interface ConfirmModalProps {
  isOpen: boolean;
  title: string;
  message: string;
  onCancel: () => void;
  onConfirm: () => void;
}

const EditModal: React.FC<EditModalProps> = ({ isOpen, title, initialValue, onClose, onSave }) => {
  const [value, setValue] = useState(initialValue);
  const inputRef = useRef<HTMLTextAreaElement>(null);
  
  useEffect(() => {
    setValue(initialValue);
    if (isOpen && inputRef.current) {
      setTimeout(() => {
        inputRef.current?.focus();
        inputRef.current?.select();
      }, 100);
    }
  }, [initialValue, isOpen]);
  
  if (!isOpen) return null;
  
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 w-full max-w-md shadow-xl transform transition-all">
        <h3 className="text-lg font-medium text-gray-900 mb-3">{title}</h3>
        
        <textarea
          ref={inputRef}
          className="w-full h-32 p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          placeholder="Enter your text here..."
        />
        
        <div className="mt-5 flex justify-end gap-3">
          <button
            type="button"
            className="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary"
            onClick={onClose}
          >
            Cancel
          </button>
          <button
            type="button"
            className="px-4 py-2 text-sm font-medium text-white bg-primary rounded-md hover:bg-primary-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary"
            onClick={() => {
              if (value.trim()) {
                onSave(value);
              }
            }}
          >
            Save
          </button>
        </div>
      </div>
    </div>
  );
};

const ConfirmModal: React.FC<ConfirmModalProps> = ({ isOpen, title, message, onCancel, onConfirm }) => {
  if (!isOpen) return null;
  
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 w-full max-w-md shadow-xl transform transition-all">
        <h3 className="text-lg font-medium text-gray-900 mb-2">{title}</h3>
        <p className="text-gray-600 mb-6">{message}</p>
        
        <div className="mt-5 flex justify-end gap-3">
          <button
            type="button"
            className="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary"
            onClick={onCancel}
          >
            Cancel
          </button>
          <button
            type="button"
            className="px-4 py-2 text-sm font-medium text-white bg-red-500 rounded-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
            onClick={onConfirm}
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  );
};

const SimpleCytoscapeGraph: React.FC<SimpleCytoscapeGraphProps> = ({ onNodeSelect }) => {
  const cyRef = useRef<HTMLDivElement>(null);
  const [cyInstance, setCyInstance] = useState<cytoscape.Core | null>(null);
  const [selectedNode, setSelectedNode] = useState<string | null>(null);
  const [selectedEdge, setSelectedEdge] = useState<string | null>(null);
  const [drawMode, setDrawMode] = useState<'none' | 'node' | 'edge'>('none');
  const [sourceNode, setSourceNode] = useState<string | null>(null);
  
  // State for edit modal
  const [isEditModalOpen, setIsEditModalOpen] = useState(false);
  const [editModalTitle, setEditModalTitle] = useState('');
  const [editModalValue, setEditModalValue] = useState('');
  const [editModalCallback, setEditModalCallback] = useState<(value: string) => void>(() => () => {});
  
  // State for confirm modal
  const [isConfirmModalOpen, setIsConfirmModalOpen] = useState(false);
  const [confirmModalTitle, setConfirmModalTitle] = useState('');
  const [confirmModalMessage, setConfirmModalMessage] = useState('');
  const [confirmModalCallback, setConfirmModalCallback] = useState<() => void>(() => () => {});
  
  // State for draggable toolbar
  const [toolbarPosition, setToolbarPosition] = useState({ x: 20, y: 20 });
  const [isDragging, setIsDragging] = useState(false);
  const [dragOffset, setDragOffset] = useState({ x: 0, y: 0 });
  const toolbarRef = useRef<HTMLDivElement>(null);

  // Initialize and configure Cytoscape
  useEffect(() => {
    if (!cyRef.current) {
      console.error("Cytoscape container not found");
      return;
    }

    console.log("Initializing Simple Cytoscape");
    
    try {
      const cy = cytoscape({
        container: cyRef.current,
        elements: [
          ...initialData.nodes.map(node => ({
            data: { id: node.id, label: node.label },
            position: node.position || { x: 0, y: 0 }
          })),
          ...initialData.edges.map(edge => ({
            data: {
              id: edge.id,
              source: edge.source,
              target: edge.target,
              label: edge.label
            }
          }))
        ],
        style: [
          {
            selector: 'node',
            style: {
              'background-color': '#e75a7c',
              'label': 'data(label)',
              'color': '#fff',
              'text-valign': 'center',
              'width': '110',
              'height': '40',
              'font-size': '14px',
              'shape': 'round-rectangle',
              'text-wrap': 'wrap',
              'text-max-width': '100',
              'padding': '25',
              'font-family': 'Quicksand, sans-serif'
            }
          },
          {
            selector: 'edge',
            style: {
              'width': 3,
              'line-color': '#d1406f',
              'target-arrow-color': '#d1406f',
              'target-arrow-shape': 'triangle',
              'curve-style': 'bezier',
              'font-size': '10px',
              'text-rotation': 'autorotate',
              'text-margin-y': -10,
              'label': 'data(label)'
            }
          },
          {
            selector: ':selected',
            style: {
              'background-color': '#ffbe0b',
              'line-color': '#ffbe0b',
              'target-arrow-color': '#ffbe0b',
              'border-width': 3,
              'border-color': '#ffbe0b'
            }
          }
        ],
        layout: {
          name: 'preset',
          fit: true,
          padding: 30
        },
        wheelSensitivity: 0.5
      });

      setCyInstance(cy);
      
      // Create a resize observer to ensure Cytoscape resizes correctly
      const resizeObserver = new ResizeObserver(() => {
        if (cy) {
          cy.resize();
          cy.fit();
        }
      });
      
      if (cyRef.current) {
        resizeObserver.observe(cyRef.current);
      }

      return () => {
        resizeObserver.disconnect();
        cy.destroy();
      };
    } catch (error) {
      console.error("Error initializing Cytoscape:", error);
    }
  }, []);
  
  // Set up event handlers when cyInstance or related states change
  useEffect(() => {
    if (!cyInstance) return;
    
    // Node tap handler
    const handleNodeTap = (evt: any) => {
      const node = evt.target;
      setSelectedNode(node.id());
      setSelectedEdge(null);
      
      if (drawMode === 'edge') {
        if (!sourceNode) {
          setSourceNode(node.id());
        } else {
          // Create a new edge
          const edgeId = `edge-${Date.now()}`;
          cyInstance.add({
            group: 'edges',
            data: {
              id: edgeId,
              source: sourceNode,
              target: node.id(),
              label: 'New connection'
            }
          });
          setSourceNode(null);
          setDrawMode('none');
        }
      } else if (onNodeSelect) {
        onNodeSelect(node.data('label'));
      }
    };
    
    // Edge tap handler
    const handleEdgeTap = (evt: any) => {
      const edge = evt.target;
      setSelectedEdge(edge.id());
      setSelectedNode(null);
    };
    
    // Canvas tap handler
    const handleCanvasTap = (evt: any) => {
      if (evt.target === cyInstance) {
        console.log('Canvas clicked, draw mode:', drawMode);
        setSelectedNode(null);
        setSelectedEdge(null);
        
        // If in node draw mode, add a new node at click position
        if (drawMode === 'node') {
          console.log('Adding node from canvas click');
          
          // Use pointer event coordinates if available
          let position = { x: 400, y: 300 }; // Default position
          
          if (evt.position) {
            position = evt.position;
            console.log('Using event position:', position);
          } else if (evt.renderedPosition) {
            position = evt.renderedPosition;
            console.log('Using rendered position:', position);
          } else {
            console.log('Using default position:', position);
          }
          
          const nodeId = `node-${Date.now()}`;
          console.log('Creating node with ID:', nodeId);
          
          cyInstance.add({
            group: 'nodes',
            data: { 
              id: nodeId, 
              label: 'New thought\n______________\n\nClick edit to change' 
            },
            position: position
          });
          
          console.log('Node added');
          setDrawMode('none');
        }
        
        // Reset source node if in edge draw mode
        if (drawMode === 'edge') {
          setSourceNode(null);
        }
      }
    };
    
    // Add event listeners
    cyInstance.on('tap', 'node', handleNodeTap);
    cyInstance.on('tap', 'edge', handleEdgeTap);
    cyInstance.on('tap', handleCanvasTap);
    
    // Cleanup event listeners
    return () => {
      cyInstance.removeListener('tap', 'node', handleNodeTap);
      cyInstance.removeListener('tap', 'edge', handleEdgeTap);
      cyInstance.removeListener('tap', handleCanvasTap);
    };
  }, [cyInstance, drawMode, onNodeSelect, sourceNode]);
  
  // Start dragging the toolbar
  const handleToolbarMouseDown = (e: React.MouseEvent) => {
    if (toolbarRef.current) {
      e.preventDefault();
      e.stopPropagation();
      
      // Calculate the offset from the toolbar's top-left corner
      setDragOffset({
        x: e.clientX - toolbarPosition.x,
        y: e.clientY - toolbarPosition.y
      });
      
      setIsDragging(true);
    }
  };
  
  // Setup drag handlers for toolbar
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (isDragging) {
        e.preventDefault();
        
        // Calculate new position based on mouse position minus the original offset
        const newX = e.clientX - dragOffset.x;
        const newY = e.clientY - dragOffset.y;
        
        // Keep toolbar within window bounds
        const maxX = window.innerWidth - (toolbarRef.current?.offsetWidth || 100);
        const maxY = window.innerHeight - (toolbarRef.current?.offsetHeight || 100);
        
        setToolbarPosition({
          x: Math.max(0, Math.min(newX, maxX)),
          y: Math.max(0, Math.min(newY, maxY))
        });
      }
    };
    
    const handleMouseUp = (e: MouseEvent) => {
      if (isDragging) {
        e.preventDefault();
        setIsDragging(false);
      }
    };
    
    if (isDragging) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);
    }
    
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  }, [isDragging, dragOffset]);

  // Helper function to open the edit modal
  const openEditModal = (title: string, initialValue: string, callback: (value: string) => void) => {
    setEditModalTitle(title);
    setEditModalValue(initialValue);
    setEditModalCallback(() => callback);
    setIsEditModalOpen(true);
  };
  
  // Helper function to open the confirm modal
  const openConfirmModal = (title: string, message: string, callback: () => void) => {
    setConfirmModalTitle(title);
    setConfirmModalMessage(message);
    setConfirmModalCallback(() => callback);
    setIsConfirmModalOpen(true);
  };

  // Handle node editing
  const handleEditNode = () => {
    if (!selectedNode || !cyInstance) return;
    
    const node = cyInstance.getElementById(selectedNode);
    const currentLabel = node.data('label');
    
    openEditModal('Edit Thought', currentLabel, (newLabel) => {
      if (newLabel.trim() !== '') {
        node.data('label', newLabel);
      }
    });
  };

  // Handle edge editing
  const handleEditEdge = () => {
    if (!selectedEdge || !cyInstance) return;
    
    const edge = cyInstance.getElementById(selectedEdge);
    const currentLabel = edge.data('label') || '';
    
    openEditModal('Edit Connection', currentLabel, (newLabel) => {
      edge.data('label', newLabel);
    });
  };

  // Handle node deletion
  const handleDeleteNode = () => {
    if (!selectedNode || !cyInstance) return;
    
    openConfirmModal(
      'Delete Thought',
      'Are you sure you want to remove this thought? This action cannot be undone.',
      () => {
        cyInstance.remove(`#${selectedNode}`);
        setSelectedNode(null);
      }
    );
  };

  // Handle edge deletion
  const handleDeleteEdge = () => {
    if (!selectedEdge || !cyInstance) return;
    
    openConfirmModal(
      'Delete Connection',
      'Are you sure you want to remove this connection? This action cannot be undone.',
      () => {
        cyInstance.remove(`#${selectedEdge}`);
        setSelectedEdge(null);
      }
    );
  };

  // Toggle drawing mode
  const toggleDrawMode = (mode: 'node' | 'edge') => {
    console.log(`Toggling draw mode to: ${mode}`);
    if (drawMode === mode) {
      setDrawMode('none');
    } else {
      setDrawMode(mode);
    }
  };

  // Prevent event propagation to the canvas
  const handleButtonClick = (e: React.MouseEvent, callback: () => void) => {
    e.stopPropagation();
    callback();
  };

  return (
    <div className="relative w-full h-full border border-gray-300 rounded-lg overflow-hidden">
      {/* Draggable Toolbar */}
      <div 
        ref={toolbarRef}
        className="absolute z-10 cursor-move"
        style={{ 
          left: `${toolbarPosition.x}px`, 
          top: `${toolbarPosition.y}px`
        }}
      >
        <div 
          className="bg-white px-1 py-0.5 rounded-t-md shadow-sm flex justify-center"
          onMouseDown={handleToolbarMouseDown}
        >
          <div className="w-16 h-1 bg-gray-300 rounded-full my-1"></div>
        </div>
        <div className="bg-white p-2 rounded-md shadow-lg flex gap-2 pointer-events-auto">
          <button 
            className={`tooltip p-2 rounded-full ${drawMode === 'node' ? 'bg-primary text-white' : 'bg-gray-100 hover:bg-gray-200'}`}
            onClick={(e) => handleButtonClick(e, () => toggleDrawMode('node'))}
            aria-label="Add a new thought"
          >
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
            </svg>
            <span className="tooltip-text">Add thought</span>
          </button>
          
          <button 
            className={`tooltip p-2 rounded-full ${drawMode === 'edge' ? 'bg-primary text-white' : 'bg-gray-100 hover:bg-gray-200'}`}
            onClick={(e) => handleButtonClick(e, () => toggleDrawMode('edge'))}
            aria-label="Connect thoughts"
          >
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101" />
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10.172 13.828a4 4 0 005.656 0l4-4a4 4 0 10-5.656-5.656l-1.102 1.101" />
            </svg>
            <span className="tooltip-text">Connect thoughts</span>
          </button>
          
          {selectedNode && (
            <>
              <button 
                className="tooltip p-2 rounded-full bg-accent hover:bg-yellow-500 text-dark"
                onClick={(e) => handleButtonClick(e, () => handleEditNode())}
                aria-label="Edit thought"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
                <span className="tooltip-text">Edit thought</span>
              </button>
              
              <button 
                className="tooltip p-2 rounded-full bg-red-400 hover:bg-red-500 text-white"
                onClick={(e) => handleButtonClick(e, handleDeleteNode)}
                aria-label="Delete thought"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
                <span className="tooltip-text">Delete thought</span>
              </button>
            </>
          )}
          
          {selectedEdge && (
            <>
              <button 
                className="tooltip p-2 rounded-full bg-accent hover:bg-yellow-500 text-dark"
                onClick={(e) => handleButtonClick(e, handleEditEdge)}
                aria-label="Edit connection"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
                <span className="tooltip-text">Edit connection</span>
              </button>
              
              <button 
                className="tooltip p-2 rounded-full bg-red-400 hover:bg-red-500 text-white"
                onClick={(e) => handleButtonClick(e, handleDeleteEdge)}
                aria-label="Delete connection"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
                <span className="tooltip-text">Delete connection</span>
              </button>
            </>
          )}
        </div>
      </div>

      <div 
        ref={cyRef}
        id="cy" 
        className="w-full h-full focus:outline-none"
        tabIndex={-1}
        style={{ 
          position: 'absolute', 
          top: 0, 
          left: 0, 
          right: 0, 
          bottom: 0,
          height: '100%',
          display: 'block'
        }}
      />
      <div className="absolute bottom-4 right-4 bg-white px-3 py-2 rounded-lg shadow text-sm">
        Click on nodes to interact
      </div>
      
      {/* Custom Edit Modal */}
      <EditModal
        isOpen={isEditModalOpen}
        title={editModalTitle}
        initialValue={editModalValue}
        onClose={() => setIsEditModalOpen(false)}
        onSave={(value) => {
          editModalCallback(value);
          setIsEditModalOpen(false);
        }}
      />
      
      {/* Custom Confirm Modal */}
      <ConfirmModal
        isOpen={isConfirmModalOpen}
        title={confirmModalTitle}
        message={confirmModalMessage}
        onCancel={() => setIsConfirmModalOpen(false)}
        onConfirm={() => {
          confirmModalCallback();
          setIsConfirmModalOpen(false);
        }}
      />
    </div>
  );
};

export default SimpleCytoscapeGraph; 