{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "57334423-0c4a-455e-aada-bd98df144d7d",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "\n",
    "#These are basic Python unit tests; they don't require a running Databricks pipelin\n",
    "def test_valid_total_calculation():\n",
    "    quantity = 2\n",
    "    unit_price = 100.0\n",
    "    total_amount = 200.0\n",
    "\n",
    "    assert abs(total_amount - (quantity * unit_price)) < 0.01\n",
    "\n",
    "\n",
    "def test_invalid_total_calculation():\n",
    "    quantity = 2\n",
    "    unit_price = 100.0\n",
    "    total_amount = 250.0\n",
    "\n",
    "    assert abs(total_amount - (quantity * unit_price)) >= 0.01\n",
    "\n",
    "\n",
    "def test_invalid_quantity():\n",
    "    quantity = 0\n",
    "\n",
    "    assert quantity <= 0\n",
    "\n",
    "\n",
    "def test_valid_quantity():\n",
    "    quantity = 3\n",
    "\n",
    "    assert quantity > 0"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "6"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "pythonIndentUnit": 4
   },
   "notebookName": "test_sales.py",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}