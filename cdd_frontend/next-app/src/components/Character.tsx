import React from 'react';
import Image from 'next/image';

interface CharacterProps {
  image: string;
}

const Character: React.FC<CharacterProps> = ({ image }) => {
  return (
    <div className="flex justify-center">
      <div className="relative">
        <div className="absolute -top-2 -right-2 w-8 h-8 bg-yellow-400 rounded-full flex items-center justify-center animate-pulse">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-white" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
          </svg>
        </div>
        <Image 
          src={image} 
          alt="Character" 
          width={150} 
          height={180}
          className="rounded-lg shadow-lg border-4 border-white"
          priority
        />
      </div>
    </div>
  );
};

export default Character; 