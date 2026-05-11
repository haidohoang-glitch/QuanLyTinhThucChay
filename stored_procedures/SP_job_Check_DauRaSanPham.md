# Stored Procedure: `job_Check_DauRaSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-14 10:13:25.983000
- **Ngày sửa cuối**: 2017-10-14 10:13:25.983000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE job_Check_DauRaSanPham
AS
    BEGIN
        DECLARE @NgayDanhSo DATETIME = '2016-01-01' ,
            @NgayBatDau DATETIME ,
            @NgayKetThuc DATETIME;
        SET @NgayBatDau = CONVERT(DATE, GETDATE());
        SET @NgayKetThuc = @NgayBatDau;
        EXEC sp_CheckDauRaChiPhiKhac_v1 @NgayDanhSo, @NgayBatDau, @NgayKetThuc;
        EXEC sp_CheckDauRaChiPhiSanPhamChinh_v1 @NgayDanhSo, @NgayBatDau,
            @NgayKetThuc;
        EXEC sp_CheckDauRaSanPhamAdmatic @NgayDanhSo, @NgayBatDau,
            @NgayKetThuc;
        EXEC sp_CheckDauRaSanPhamCPD_v1 @NgayDanhSo, @NgayBatDau, @NgayKetThuc;
        EXEC sp_CheckDauRaSanPhamCPM_v1 @NgayDanhSo, @NgayBatDau, @NgayKetThuc;
        EXEC sp_CheckDauRaSanPhamGGFB_v1 @NgayDanhSo, @NgayBatDau,
            @NgayKetThuc;
        EXEC sp_CheckDauRaSanPhamMobile_v1 @NgayDanhSo, @NgayBatDau,
            @NgayKetThuc;
        EXEC sp_CheckDauRaSanPhamMuaNgoai_v1 @NgayDanhSo, @NgayBatDau,
            @NgayKetThuc;
        EXEC sp_CheckDauRaSanPhamPR_v1 @NgayDanhSo, @NgayBatDau, @NgayKetThuc;


    END;
```
