import React from 'react';

interface TextBubbleProps {
  message: string;
}

const TextBubble: React.FC<TextBubbleProps> = ({ message }) => {
  return (
    <div className="bg-secondary bg-opacity-10 p-5 rounded-2xl shadow-md relative mt-4 mb-6 w-fit max-w-[90%] border-l-4 border-primary">
      <div className="absolute -bottom-4 left-6 w-0 h-0 border-l-8 border-r-8 border-t-8 border-transparent border-t-secondary border-opacity-10"></div>
      <p className="text-gray-700 font-sans text-lg">{message}</p>
    </div>
  );
};

export default TextBubble; 