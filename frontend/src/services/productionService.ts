import api from './api';

export const productionService = {
    getWorkOrders: async () => {
        const response = await api.get('/production/orders');
        return response.data;
    },
};
