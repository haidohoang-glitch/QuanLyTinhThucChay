# Stored Procedure: `BPTC_NhapChiTieu_Get_DanhSachLoaiTien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:50.117000
- **Ngày sửa cuối**: 2015-06-11 18:17:50.117000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_NhapChiTieu_Get_DanhSachLoaiTien]
AS 
    BEGIN
        CREATE TABLE #T
            (
              Id INT ,
              Name NVARCHAR(100)
            )
        
        INSERT  INTO #T ( Id, Name ) VALUES  ( 2, N'Đánh số' )    
        INSERT  INTO #T ( Id, Name ) VALUES  ( 3, N'Bản cứng' )
        INSERT  INTO #T ( Id, Name ) VALUES  ( 1, N'Thực chạy' )
        INSERT  INTO #T ( Id, Name ) VALUES  ( 4, N'Hóa đơn' )
        
        SELECT  *
        FROM    #T
        DROP TABLE #T
    END


```
