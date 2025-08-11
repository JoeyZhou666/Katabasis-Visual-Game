import React from 'react';
import Image from 'next/image';
import Link from 'next/link';

const Navbar: React.FC = () => {
  return (
    <nav className="bg-white shadow-md px-6 py-3 flex items-center border-b-2 border-primary border-opacity-30">
      <div className="flex-shrink-0 mr-6">
        <Image src="/images/logo.png" alt="Logo" width={120} height={40} />
      </div>
      
      <h1 className="text-2xl font-bold text-primary mr-auto font-heading">My Thought Map</h1>
      
      <ul className="flex gap-6">
        <li>
          <Link href="/" className="text-primary hover:text-primary hover:underline font-medium transition-colors">
            Home
          </Link>
        </li>
        <li>
          <Link href="/about" className="text-gray-600 hover:text-primary font-medium transition-colors">
            About
          </Link>
        </li>
        <li>
          <Link href="/resources" className="text-gray-600 hover:text-primary font-medium transition-colors">
            Resources
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar; 