import api from './api';

export const crmService = {
    getCustomers: async () => {
        const response = await api.get('/crm/customers');
        return response.data;
    },
};
