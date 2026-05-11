# Function: `ThucChay_TinhGiaTriThayDoi`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-04 11:52:22.547000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.323000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@NgayThayDoi` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |
| `@HopDongFK` | `nvarchar(100)` | No |
| `@ThanhTienHienTai` | `float(8)` | No |
| `@SoNgayHienTai` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_TinhGiaTriThayDoi]
(
	@DonViTinh NVARCHAR(50),
	@NgayThayDoi DATETIME,
	@HopDongChiTietID nvarchar(50),
	@HopDongFK  NVARCHAR(50),
	@ThanhTienHienTai FLOAT,
	@SoNgayHienTai INT
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result FLOAT
	
	DECLARE @DonGiaChenhLech FLOAT, @DonGiaLienKeTruoc FLOAT, @SoLuongThucChay FLOAT
	DECLARE @ThanhTienSauTrietKhauLKTruoc FLOAT
	DECLARE @SoNgayLienKeTruoc FLOAT, @DonGia FLOAT, @TinhGiaTriThayDoiYN NVARCHAR(50)
	SET @TinhGiaTriThayDoiYN = 
			dbo.ThucChay_HopDongChiTietCoThayDoiGiaSauTrietKhauYN(CONVERT(INT,@HopDongChiTietID),@NgayThayDoi)
	SET @Result = 0;
	IF(@TinhGiaTriThayDoiYN = 'Y')
	BEGIN
		IF(@DonViTinh = N'TUẦN' OR @DonViTinh = N'THÁNG' OR @DonViTinh = N'NGÀY' OR @DonViTinh = N'NĂM')
	
		BEGIN
			--Tinh DonGiaLienKeTruoc ? ThanhtiensautrietkhauTruoc/SoNgay
			SET @ThanhTienSauTrietKhauLKTruoc = (
										SELECT TOP 1 ThanhTien FROM 
										dbo.GetHopDongChiTietThayDoiAll() 
										WHERE 
										HopDongChiTietID =	@HopDongChiTietID AND 
										HopDongFK = @HopDongFK AND 
										NgayThayDoi < @NgayThayDoi
										ORDER BY NgayThayDoi DESC
			)
			--So ngay Lien ke truoc
			SET @SoNgayLienKeTruoc = (
										SELECT TOP 1 tcdt.SoLuong FROM ThucChayDaTinh tcdt
										WHERE tcdt.NgayThucHien < @NgayThayDoi
										AND dbo.FormatString(TCDT.HopDongChiTietREF) = @HopDongChiTietID
										ORDER BY TCDT.NgayThucHien DESC	
			)
			
			IF(@SoNgayLienKeTruoc = 0)
				SET @DonGiaLienKeTruoc = 0
			ELSE
				SET @DonGiaLienKeTruoc = @ThanhTienSauTrietKhauLKTruoc/@SoNgayLienKeTruoc
			
			--So ngay hien tai
			IF(@SoNgayHienTai = 0)
				SET @DonGia = 0;
			ELSE	
				set @DonGia = @ThanhTienHienTai/@SoNgayHienTai
			 							 
			SET @DonGiaChenhLech = @DonGia - @DonGiaLienKeTruoc
			
			SET @SoLuongThucChay = 	(	
										SELECT ISNULL(sum(tcdt.SoLuongThucChay),0) 
										FROM ThucChayDaTinh tcdt
										WHERE tcdt.NgayThucHien < @NgayThayDoi
										AND dbo.FormatString(TCDT.HopDongChiTietREF) = @HopDongChiTietID
			)
			
			SET @Result = @SoLuongThucChay * @DonGiaChenhLech
		END
	ELSE --Tinh chenh lech cho hinh thuc san pham la CPM
		BEGIN
			SET @Result = 0;
		END
	END
	-- Return the result of the function
	RETURN @Result

END

```
