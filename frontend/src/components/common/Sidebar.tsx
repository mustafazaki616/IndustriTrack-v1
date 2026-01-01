import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar: React.FC = () => {
    return (
        <aside className="sidebar">
            <nav>
                <ul>
                    <li><Link to="/">Dashboard</Link></li>
                    <li><Link to="/inventory">Inventory</Link></li>
                    <li><Link to="/production">Production</Link></li>
                    <li><Link to="/crm">CRM</Link></li>
                </ul>
            </nav>
        </aside>
    );
};

export default Sidebar;
