import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface ProductionState {
    orders: any[];
}

const initialState: ProductionState = {
    orders: [],
};

const productionSlice = createSlice({
    name: 'production',
    initialState,
    reducers: {
        setOrders: (state, action: PayloadAction<any[]>) => {
            state.orders = action.payload;
        },
    },
});

export const { setOrders } = productionSlice.actions;
export default productionSlice.reducer;
Jonah
Jonah
Jonah
