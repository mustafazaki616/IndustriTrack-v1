import React from 'react';
import Header from '../components/common/Header';
import Sidebar from '../components/common/Sidebar';

const DashboardPage: React.FC = () => {
    return (
        <div className="layout">
            <Sidebar />
            <div className="main-content">
                <Header />
                <main>
                    <h2>Dashboard</h2>
                    <p>Welcome to your IndustriTrack Dashboard.</p>
                </main>
            </div>
        </div>
    );
};

export default DashboardPage;
