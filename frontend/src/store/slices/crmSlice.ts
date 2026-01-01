import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface CRMState {
    customers: any[];
}

const initialState: CRMState = {
    customers: [],
};

const crmSlice = createSlice({
    name: 'crm',
    initialState,
    reducers: {
        setCustomers: (state, action: PayloadAction<any[]>) => {
            state.customers = action.payload;
        },
    },
});

export const { setCustomers } = crmSlice.actions;
export default crmSlice.reducer;
Jonah
Jonah
Jonah
Jonah
Jonah
