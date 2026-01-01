import { User, Product } from './index';

export interface InventoryItem {
    id: number;
    product: Product;
    quantity: number;
}

export interface WorkOrder {
    id: number;
    productId: number;
    quantity: number;
    status: string;
}
Jonah
