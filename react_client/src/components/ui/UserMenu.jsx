import React, { useState, useRef, useEffect } from "react";
import { User } from "lucide-react"; // nice icon from lucide-react

export default function UserMenu() {
  const [open, setOpen] = useState(false);
  const menuRef = useRef(null);

  // Close menu if clicked outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (menuRef.current && !menuRef.current.contains(event.target)) {
        setOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div className="relative inline-block text-left" ref={menuRef}>
      <button
        onClick={() => setOpen((prev) => !prev)}
        className="flex items-center space-x-2 bg-gray-100 hover:bg-gray-200 rounded-full px-3 py-2 shadow"
      >
        <div className="w-8 h-8 bg-blue-500 text-white rounded-full flex items-center justify-center">
          <User size={18} />
        </div>
        <span className="font-medium">John Doe</span>
      </button>

      {open && (
        <div className="absolute right-0 mt-2 w-40 bg-white rounded-lg shadow-lg border p-2 z-10">
          <button className="w-full text-left px-3 py-2 rounded hover:bg-gray-100">
            View Profile
          </button>
          <button className="w-full text-left px-3 py-2 rounded hover:bg-gray-100">
            Settings
          </button>
          <button className="w-full text-left px-3 py-2 rounded text-red-500 hover:bg-red-100">
            Logout
          </button>
        </div>
      )}
    </div>
  );
}
