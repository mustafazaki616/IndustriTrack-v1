# React Frontend Development Rules

## Technology Stack
- **Framework**: React 18
- **Language**: TypeScript
- **State Management**: Redux Toolkit (Global), React Hooks (Local)
- **Styling**: Tailwind CSS
- **HTTP Client**: Axios

## Component Patterns
- **Functional Components**: Use `React.FC<Props>` or directly typed props.
- **Hooks**: Use custom hooks for logic reuse.
- **Naming**: PascalCase for components, camelCase for variables/functions.

## State Management
- **Redux Toolkit**: Use slices for global application state (User, Theme, complex data).
- **Local State**: Use `useState` or `useReducer` for component-specific UI state.

## API Integration
- All API calls must go through the `src/services/` layer.
- Handle errors gracefully using `try-catch` blocks or interceptors.

## Styling
- Use **Tailwind CSS** utility classes.
- Design **Mobile-First**: Base styles are mobile, use `md:`, `lg:` prefixes for larger screens.
- Avoid inline styles.

### Example Component

```tsx
import React, { useState, useEffect } from 'react';
import { useAppDispatch, useAppSelector } from '../../hooks/redux';
import { fetchProducts } from '../../store/slices/productSlice';
import { Product } from '../../types/models';

interface ProductListProps {
  categoryId: string;
}

const ProductList: React.FC<ProductListProps> = ({ categoryId }) => {
  const dispatch = useAppDispatch();
  const { items, isLoading, error } = useAppSelector((state) => state.products);

  useEffect(() => {
    dispatch(fetchProducts(categoryId));
  }, [dispatch, categoryId]);

  if (isLoading) return <div className="p-4 text-center">Loading...</div>;
  if (error) return <div className="p-4 text-red-500">Error: {error}</div>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {items.map((product: Product) => (
        <div key={product.id} className="border rounded-lg p-4 shadow-sm hover:shadow-md transition-shadow">
          <h3 className="text-xl font-bold mb-2">{product.name}</h3>
          <p className="text-gray-600">${product.price}</p>
        </div>
      ))}
    </div>
  );
};

export default ProductList;
```
