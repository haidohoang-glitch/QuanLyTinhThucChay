# Stored Procedure: `Admarket_ThucChayAdmarketCanPhanBoUpdateGiamGiaTri`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-29 15:38:35.367000
- **Ngày sửa cuối**: 2016-03-31 11:50:12.223000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	Cân th?c ch?y khi phân b? update giá tr? gi?m di
-- =============================================
CREATE PROCEDURE [dbo].[Admarket_ThucChayAdmarketCanPhanBoUpdateGiamGiaTri]
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	-- Insert statements for procedure here
	DECLARE @SoHopDong NVARCHAR(50)
	DECLARE @PhanBoID INT 
	DECLARE @DmSanPhamREF INT
	DECLARE @TenSanPham NVARCHAR(200)
	DECLARE @DmListNhanHangREF NVARCHAR(200)
	DECLARE @ThanhTienPhanBo FLOAT,
	        @ThanhTienThucChay FLOAT
	
	DECLARE @ChenhLech FLOAT
	DECLARE @Tk_Admarket     NVARCHAR(50),
	        @Tk_Admarket_ID  NVARCHAR(50)
	
	DECLARE db_cursor CURSOR  
	FOR
	    SELECT hd.SoHopDong,
	           hdct.HopDongChiTietID,
	           hdct.DmSanPhamREF,
	           hdct.TenSanPham,
	           hdct.DanhSachNhanHangREF,
	           hdct.ThanhTien,
	           hdct.TK_AdMarket,
	           hdct.TK_AdMarketID
	    FROM   HopDongChiTiet hdct
	           INNER JOIN HopDong hd
	                ON  hd.HopDongID = hdct.HopDongFK
	    WHERE  CONVERT(DATE, hdct.LastModifiedAt) = CONVERT(DATE, @NgayThucHien)
	           AND hdct.DmSanPhamREF IN (144, 628, 585)
	           AND dbo.fn_CheckIsDmLoaiHopDongNoiBo(hd.DmMaHopDongREF, hd.NgayDanhSoHopDong) = 
	               0
	
	OPEN db_cursor 
	FETCH NEXT FROM db_cursor INTO @SoHopDong,@PhanBoID,@DmSanPhamREF,@TenSanPham,
	@DmListNhanHangREF ,@ThanhTienPhanBo ,@Tk_Admarket, @Tk_Admarket_ID
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
	    SELECT @ThanhTienThucChay = ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay + A.GiaTriThayDoi), 0)
	    FROM   ThucChayDaTinhAdmarket A
	    WHERE  A.HopDongChiTietREF = @PhanBoID
	           AND A.DmSanPhamREF = @DmSanPhamREF
	           AND A.NgayThucHien <= @NgayThucHien
	    
	    IF @ThanhTienThucChay > @ThanhTienPhanBo
	    BEGIN
	        SET @ChenhLech = @ThanhTienThucChay -@ThanhTienPhanBo 
	        EXEC dbo.Admarket_ThucChayDaTinhAdmarket_NhanHang_InsertByPhanBoID_GTTD 
	             @NgayThucHien,
	             @SoHopDong,
	             @PhanBoID,
	             @DmSanPhamREF,
	             @TenSanPham,
	             0 --@DmWebsiteREF
	             ,
	             '' --@TenWebsite
	             ,
	             0,
	             0,
	             0,
	             @ChenhLech,
	             0,
	             0,
	             0,
	             0,
	             0,
	             'CPC',
	             'Phan bo thay doi gia tri',
	             1,
	             '',
	             @DmListNhanHangREF
	        
	        -- insert online
	        INSERT INTO dbo.ThucChayAdmarketUser_NhanHang_Online
	        SELECT NEWID(),
	               @Tk_Admarket,
	               @DmSanPhamREF,
	               @TenSanPham,
	               '',
	               0,
	               0,
	               @ChenhLech,
	               0,
	               0,
	               @NgayThucHien,
	               GETDATE(),
	               'Doannv',
	               GETDATE(),
	               'Doannv',
	               @Tk_Admarket_ID,
	               0,
	               ''
	    END
	    
	    FETCH NEXT FROM db_cursor INTO @SoHopDong,@PhanBoID,@DmSanPhamREF,@TenSanPham,
	    @DmListNhanHangREF ,@ThanhTienPhanBo ,@Tk_Admarket, @Tk_Admarket_ID
	END 
	
	CLOSE db_cursor 
	DEALLOCATE db_cursor
END

```
