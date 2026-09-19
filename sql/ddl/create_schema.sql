IF NOT EXISTS (SELECT 1 FROM sys.schemas WHERE name = N'schema')
    EXEC('CREATE SCHEMA schema');
