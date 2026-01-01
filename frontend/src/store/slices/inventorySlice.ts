import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface InventoryState {
    items: any[];
}

const initialState: InventoryState = {
    items: [],
};

const inventorySlice = createSlice({
    name: 'inventory',
    initialState,
    reducers: {
        setInventory: (state, action: PayloadAction<any[]>) => {
            state.items = action.payload;
        },
    },
});

export const { setInventory } = inventorySlice.actions;
export default inventorySlice.reducer;
Jonah
Jonah
