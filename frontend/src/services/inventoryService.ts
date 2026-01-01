import api from './api';

export const inventoryService = {
    getInventory: async () => {
        const response = await api.get('/inventory');
        return response.data;
    },
};
