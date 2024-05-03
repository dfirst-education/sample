sp_configure 'show advanced options', 1
go
reconfigure with override
go
sp_configure 'max server memory', 4096
go
reconfigure with override
go

sp_configure
go