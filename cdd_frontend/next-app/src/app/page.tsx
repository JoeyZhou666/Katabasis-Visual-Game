'use client';

import React from 'react';
import Character from '@/components/Character';
import TextBubble from '@/components/TextBubble';
import dynamic from 'next/dynamic';

// Import the SimpleCytoscapeGraph with SSR disabled
const SimpleCytoscapeGraph = dynamic(() => import('@/components/SimpleCytoscapeGraph'), { 
  ssr: false,
  loading: () => (
    <div className="flex items-center justify-center h-full w-full bg-white bg-opacity-50 rounded-lg p-6">
      <div className="text-center">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary mx-auto mb-4"></div>
        <p className="text-primary font-medium">Loading your Thought Map...</p>
      </div>
    </div>
  )
});

export default function Home() {
  return (
    <div className="h-screen w-screen flex items-center justify-center bg-secondary bg-opacity-20 p-4">
      <div className="w-full h-full max-w-[1800px] max-h-[900px] flex flex-col">
        <div className="flex flex-col md:flex-row gap-6 flex-1">
          {/* Left panel for character and messages */}
          <div className="w-full md:w-1/3 bg-white bg-opacity-60 rounded-lg p-6 shadow-md h-full">
            <h2 className="text-xl font-bold text-primary font-heading mb-4">Your Thought Map Guide</h2>
            <p className="text-gray-600 mb-6">Let's explore your ideas and connect them together!</p>
            <TextBubble message="Hi there! I'm your guide. Click on nodes in your thought map to explore your ideas!" />
            <div className="mt-8 flex justify-center">
              <Character image="/images/mousy smile.PNG" />
            </div>
          </div>
          
          {/* Right panel for the graph */}
          <div className="w-full md:w-2/3 bg-white bg-opacity-60 rounded-lg shadow-md overflow-hidden h-full relative">
            <SimpleCytoscapeGraph onNodeSelect={(nodeId) => {
              console.log(`Selected node: ${nodeId}`);
            }} />
          </div>
        </div>
      </div>
    </div>
  );
} 