# Stored Procedure: `BPTC_Report_BCKD_Update`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:50.387000
- **Ngày sửa cuối**: 2015-06-11 18:17:50.387000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinBCKDID` | `int(4)` | No |
| `@TrangThaiPheDuyet` | `int(4)` | No |
| `@NguoiPheDuyet` | `nvarchar(510)` | No |
| `@NoiDungDanhGia_Khoi` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_DanhSo` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_HoaDon` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_ThucChay` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_BoPhan` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_BoPhan_DanhSoHaiDau` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_SanPham` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_XuatHoaDon` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_XuatHoaDon_Nam` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_XuatHoaDon_ThucChay` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_Huy_ThayDoi` | `nvarchar(1000)` | No |
| `@NoiDungDanhGia_Huy_ThayDoi_HopDong` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Report_BCKD_Update]
    (
      @ThongTinBCKDID INT ,
      @TrangThaiPheDuyet INT ,
      @NguoiPheDuyet NVARCHAR(255) ,
      @NoiDungDanhGia_Khoi NVARCHAR(500) ,
      @NoiDungDanhGia_DanhSo NVARCHAR(500) ,
      @NoiDungDanhGia_HoaDon NVARCHAR(500) ,
      @NoiDungDanhGia_ThucChay NVARCHAR(500) ,
      @NoiDungDanhGia_BoPhan NVARCHAR(500) ,
      @NoiDungDanhGia_BoPhan_DanhSoHaiDau NVARCHAR(500) ,
      @NoiDungDanhGia_SanPham NVARCHAR(500) ,
      @NoiDungDanhGia_XuatHoaDon NVARCHAR(500) ,
      @NoiDungDanhGia_XuatHoaDon_Nam NVARCHAR(500) ,
      @NoiDungDanhGia_XuatHoaDon_ThucChay NVARCHAR(500) ,
      @NoiDungDanhGia_Huy_ThayDoi NVARCHAR(500) ,
      @NoiDungDanhGia_Huy_ThayDoi_HopDong NVARCHAR(500)
    )
AS 
    BEGIN
 	--@TrangThaiPheDuyet 0: SUBMITTED, 1: APPROVED, 2: REJECTED
        DECLARE @LastModifiedAt DATETIME
        DECLARE @NgayPheDuyet DATETIME
        DECLARE @LoaiBaoCao NVARCHAR(100)
        
        SET @LastModifiedAt = GETDATE()
        SET @NgayPheDuyet = GETDATE()
        
        SELECT  @LoaiBaoCao = LoaiBaoCaoKinhDoanh
        FROM    dbo.BPTC_ThongTinBCKD
        WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID
 		
        IF @TrangThaiPheDuyet > 0 
            BEGIN
                UPDATE  dbo.BPTC_ThongTinBCKD
                SET     TrangThaiPheDuyet = @TrangThaiPheDuyet ,
                        NguoiPheDuyet = @NguoiPheDuyet ,
                        NgayPheDuyet = @NgayPheDuyet ,
                        LastModifiedBy = @NguoiPheDuyet ,
                        LastModifiedAt = @LastModifiedAt
                WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID
            END 
        ELSE 
            BEGIN                
                UPDATE  dbo.BPTC_ThongTinBCKD
                SET     LastModifiedBy = @NguoiPheDuyet ,
                        LastModifiedAt = @LastModifiedAt
                WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID
            END
            
		--UPDATE BPTC_ThongTinBCKD_Khoi
        UPDATE  dbo.BPTC_ThongTinBCKD_Khoi
        SET     NoiDungDanhGia = @NoiDungDanhGia_Khoi ,
                LastModifiedBy = @NguoiPheDuyet ,
                LastModifiedAt = @LastModifiedAt
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
		--UPDATE BPTC_ThongTinBCKD_Khoi_DanhSo
        UPDATE  dbo.BPTC_ThongTinBCKD_Khoi_DanhSo
        SET     NoiDungDanhGia = @NoiDungDanhGia_DanhSo ,
                LastModifiedBy = @NguoiPheDuyet ,
                LastModifiedAt = @LastModifiedAt
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --UPDATE BPTC_ThongTinBCKD_Khoi_HoaDon
        UPDATE  dbo.BPTC_ThongTinBCKD_Khoi_HoaDon
        SET     NoiDungDanhGia = @NoiDungDanhGia_HoaDon ,
                LastModifiedBy = @NguoiPheDuyet ,
                LastModifiedAt = @LastModifiedAt
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --UPDATE BPTC_ThongTinBCKD_Khoi_ThucChay
        UPDATE  dbo.BPTC_ThongTinBCKD_Khoi_ThucChay
        SET     NoiDungDanhGia = @NoiDungDanhGia_ThucChay ,
                LastModifiedBy = @NguoiPheDuyet ,
                LastModifiedAt = @LastModifiedAt
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --UPDATE BPTC_ThongTinBCKD_SanPham
        UPDATE  dbo.BPTC_ThongTinBCKD_SanPham
        SET     NoiDungDanhGia = @NoiDungDanhGia_SanPham ,
                LastModifiedBy = @NguoiPheDuyet ,
                LastModifiedAt = @LastModifiedAt
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --UPDATE BPTC_ThongTinBCKD_BoPhan
        UPDATE  dbo.BPTC_ThongTinBCKD_BoPhan
        SET     NoiDungDanhGia = @NoiDungDanhGia_BoPhan ,
                LastModifiedBy = @NguoiPheDuyet ,
                LastModifiedAt = @LastModifiedAt
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --UPDATE BPTC_ThongTinBCKD_BoPhan_DanhSoHaiDau
        UPDATE  dbo.BPTC_ThongTinBCKD_BoPhan_DanhSoHaiDau
        SET     NoiDungDanhGia = @NoiDungDanhGia_BoPhan_DanhSoHaiDau ,
                LastModifiedBy = @NguoiPheDuyet ,
                LastModifiedAt = @LastModifiedAt
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        IF @LoaiBaoCao = '2' -- BAO CAO THANG
            BEGIN
				--UPDATE BPTC_ThongTinBCKD_XuatHoaDon
                UPDATE  dbo.BPTC_ThongTinBCKD_XuatHoaDon
                SET     NoiDungDanhGia = @NoiDungDanhGia_XuatHoaDon ,
                        LastModifiedBy = @NguoiPheDuyet ,
                        LastModifiedAt = @LastModifiedAt
                WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID    
                
                --UPDATE BPTC_ThongTinBCKD_XuatHoaDon_Nam
                UPDATE  dbo.BPTC_ThongTinBCKD_XuatHoaDon_Nam
                SET     NoiDungDanhGia = @NoiDungDanhGia_XuatHoaDon_Nam ,
                        LastModifiedBy = @NguoiPheDuyet ,
                        LastModifiedAt = @LastModifiedAt
                WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
                
                --UPDATE BPTC_ThongTinBCKD_XuatHoaDon_ThucChay
                UPDATE  dbo.BPTC_ThongTinBCKD_XuatHoaDon_ThucChay
                SET     NoiDungDanhGia = @NoiDungDanhGia_XuatHoaDon_ThucChay ,
                        LastModifiedBy = @NguoiPheDuyet ,
                        LastModifiedAt = @LastModifiedAt
                WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID
                
                --UPDATE BPTC_ThongTinBCKD_Huy_ThayDoi
                UPDATE  dbo.BPTC_ThongTinBCKD_Huy_ThayDoi
                SET     NoiDungDanhGia = @NoiDungDanhGia_Huy_ThayDoi ,
                        LastModifiedBy = @NguoiPheDuyet ,
                        LastModifiedAt = @LastModifiedAt
                WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID
                
                --UPDATE BPTC_ThongTinBCKD_Huy_ThayDoi_HopDong
                UPDATE  dbo.BPTC_ThongTinBCKD_Huy_ThayDoi_HopDong
                SET     NoiDungDanhGia = @NoiDungDanhGia_Huy_ThayDoi_HopDong ,
                        LastModifiedBy = @NguoiPheDuyet ,
                        LastModifiedAt = @LastModifiedAt
                WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
                            	
            END            
 	 
    END

```
