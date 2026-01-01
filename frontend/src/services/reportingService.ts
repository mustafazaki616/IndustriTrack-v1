import api from './api';

export const reportingService = {
    getDashboardData: async () => {
        const response = await api.get('/reporting/dashboard');
        return response.data;
    },
};
