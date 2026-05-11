# Stored Procedure: `BPTC_Update_ThongTinBCSP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.203000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.203000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ReportID` | `int(4)` | No |
| `@TrangThaiPheDuyet` | `int(4)` | No |
| `@NguoiPheDuyet` | `nvarchar(510)` | No |
| `@NoiDungDanhGia_DanhSo` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_ThucChay` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_ThucChay_DanhSo` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Update_ThongTinBCSP]
    (
      @ReportID INT ,
      @TrangThaiPheDuyet INT ,
      @NguoiPheDuyet NVARCHAR(255) ,
      @NoiDungDanhGia_DanhSo NVARCHAR(500) ,
      @NoiDungDanhGia_ThucChay NVARCHAR(500) ,
      @NoiDungDanhGia_ThucChay_DanhSo NVARCHAR(500)      
    )
AS 
    BEGIN
 		
 		--@TrangThaiPheDuyet 0: SUBMITTED, 1: APPROVED, 2: REJECTED
        DECLARE @LastModifiedAt DATETIME
        DECLARE @NgayPheDuyet DATETIME
                
        SET @LastModifiedAt = GETDATE()                 
        SET @NgayPheDuyet = @LastModifiedAt
 		
        IF @TrangThaiPheDuyet > 0 
            BEGIN
                UPDATE  dbo.BPTC_BaoCaoTTSanPhamThang
                SET     TrangThaiPheDuyet = @TrangThaiPheDuyet ,
                        NguoiPheDuyet = @NguoiPheDuyet ,
                        NgayPheDuyet = @NgayPheDuyet ,
                        LastModifiedBy = @NguoiPheDuyet ,
                        LastModifiedAt = @LastModifiedAt
                WHERE   BPTC_BaoCaoTTSanPhamThangID = @ReportID
            END 
        ELSE 
            BEGIN                
                UPDATE  dbo.BPTC_BaoCaoTTSanPhamThang
                SET     LastModifiedBy = @NguoiPheDuyet ,
                        LastModifiedAt = @LastModifiedAt
                WHERE   BPTC_BaoCaoTTSanPhamThangID = @ReportID
            END
            
		--UPDATE BPTC_BaoCaoTTSanPhamThang_DanhSo
        UPDATE  dbo.BPTC_BaoCaoTTSanPhamThang_DanhSo
        SET     NoiDungDanhGia = @NoiDungDanhGia_DanhSo ,
                LastModifiedBy = @NguoiPheDuyet ,
                LastModifiedAt = @LastModifiedAt
        WHERE   BPTC_BaoCaoTTSanPhamThangREF = @ReportID
        
		--UPDATE BPTC_BaoCaoTTSanPhamThang_ThucChay
        UPDATE  dbo.BPTC_BaoCaoTTSanPhamThang_ThucChay
        SET     NoiDungDanhGia = @NoiDungDanhGia_ThucChay ,
                LastModifiedBy = @NguoiPheDuyet ,
                LastModifiedAt = @LastModifiedAt
        WHERE   BPTC_BaoCaoTTSanPhamThangREF = @ReportID
        
        --UPDATE BPTC_BaoCaoTTSanPhamThang_ThucChay_DanhSo
        UPDATE  dbo.BPTC_BaoCaoTTSanPhamThang_ThucChay_DanhSo
        SET     NoiDungDanhGia = @NoiDungDanhGia_ThucChay_DanhSo ,
                LastModifiedBy = @NguoiPheDuyet ,
                LastModifiedAt = @LastModifiedAt
        WHERE   BPTC_BaoCaoTTSanPhamThangREF = @ReportID
 	 
    END

```
