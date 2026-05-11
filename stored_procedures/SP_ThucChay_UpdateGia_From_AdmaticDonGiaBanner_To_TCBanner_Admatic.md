# Stored Procedure: `ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-01-06 13:02:15.783000
- **Ngày sửa cuối**: 2023-10-06 16:18:36.353000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerREF` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic] 391390

CREATE  PROCEDURE [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic] 
	@DmBannerREF INT
AS
BEGIN
	DECLARE @DonGiaBanner_VAT FLOAT, @LoaiDonGiaTheoDVT INT, @DonViTinh NVARCHAR(50),@Vat FLOAT = 1.1
	DECLARE @BannerDateCreate DATETIME
	SELECT @DonGiaBanner_VAT =  DonGiaBanner_VAT
	, @LoaiDonGiaTheoDVT = LoaiDonGiaTheoDVT 
	,@BannerDateCreate = BannerDateCreate
	 FROM dbo.AdmaticDonGiaBanner
	WHERE DmBannerID = @DmBannerREF
	IF CONVERT(DATE,@BannerDateCreate) >= '2023-07-01' SET @Vat = 1.08;
	SET @DonGiaBanner_VAT = (ISNULL(@DonGiaBanner_VAT,0))/@Vat



	DECLARE @cdate DATETIME 

	SET @cdate = GETDATE()


	IF DATEPART(HOUR, @cdate) >= 14 AND DATEPART(HOUR, @cdate) <= 23
	BEGIN
		SET @cdate = DATEADD(DAY, 1, @cdate)
	END

	--IF(@LoaiDonGiaTheoDVT = 2 OR @LoaiDonGiaTheoDVT =3)
	--	SET @DonViTinh = 'CPM'
	--ELSE
	--	SET @DonViTinh = 'CPC'

	SET @DonViTinh = 
	(
		CASE WHEN @LoaiDonGiaTheoDVT IN (2,3) THEN 	'CPM'
			WHEN @LoaiDonGiaTheoDVT = 1 THEN 'CPC'
			WHEN @LoaiDonGiaTheoDVT = 4 THEN 'TRUE VIEW'
			WHEN @LoaiDonGiaTheoDVT = 5 THEN N'BÀI'
		ELSE ''
		END
	)

	IF(EXISTS(SELECT ThucChayHopDongChiTietID FROM dbo.ThucChayHopDongChiTietAndBanner_Admatic 
	WHERE CONVERT(INT,DmBannerID) = @DmBannerREF
	AND ISNULL(DonGia_Banner,0) <> 0))
	BEGIN
		INSERT INTO dbo.ThucChayHopDongChiTietAndBanner_Admatic_DonGiaTD
		        ( ThucChayHopDongChiTietID ,
		          DmBannerID ,
		          HopDongChiTietREF ,
		          HopDongREF ,
		          BookingREF ,
		          ThoiGianBatDau ,
		          ThoiGianKetThuc ,
		          TiLeThucChayHDCTSoVoiBanner ,
		          DaThucHienUpdateTiLe ,
		          CreatedBy ,
		          CreatedAt ,
		          LastModifiedBy ,
		          LastModifiedAt ,
		          DeletedStatus ,
		          DsNhanHangREF ,
		          DonGia_Banner ,
		          DmHinhThucQuangCaoID ,
		          DmSanPhamID ,
		          DonViTinh,
				  LogTime
		        )
		SELECT *,@cdate Logtime FROM dbo.ThucChayHopDongChiTietAndBanner_Admatic
		WHERE CONVERT(INT,DmBannerID) = @DmBannerREF
		AND isnull(DonGia_Banner,0) <> 0
	END

	UPDATE dbo.ThucChayHopDongChiTietAndBanner_Admatic
	SET DonGia_Banner = @DonGiaBanner_VAT
	, DonViTinh = @DonViTinh
	WHERE DmBannerID = @DmBannerREF
END


```
