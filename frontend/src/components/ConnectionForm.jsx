import React from "react";
import "../styles/ConnectionForm.css";
import { useNavigate } from "react-router-dom";

function ConnectionForm({ form, onDelete }) {
  const navigate = useNavigate();

  // Directly navigate and pass the form data
  const handleCatalogNavigation = () => {
    navigate(`/catalog/tables/${form.connection_id}`, { state: { form } });
  };

  return (
    <div className="connection-card">
      <h3>{form.database_name}</h3>
      <div className="connection-details">
        <p><strong>Hostname:</strong> {form.hostname}</p>
        <p><strong>Port:</strong> {form.port}</p>
        <p><strong>Username:</strong> {form.username}</p>
        <p><strong>Description:</strong> {form.description}</p>
        <p><strong>Platform:</strong> {form.platform_name}</p>
        <p><strong>Role:</strong> {form.role_name}</p>
        <p><strong>Department:</strong> {form.department_name}</p>
      </div>
      <div className="connection-actions">
        <button onClick={handleCatalogNavigation} className="tables-button">
          View Data Catalog
        </button>
        <button onClick={() => onDelete(form.connection_id)} className="delete-button">
          Delete
        </button>
      </div>
    </div>
  );
}

export default ConnectionForm;
