# Stored Procedure: `ThucChayDaTinh_CheckKetQuaVanHanhXoa_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-25 16:34:10.053000
- **Ngày sửa cuối**: 2021-12-03 16:24:26.183000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-13
-- Description:	<Description,,>
-- =============================================
/*
	EXEC [ThucChayDaTinh_CheckKetQuaVanHanhXoa_CreatorContent] '2020-10-19'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_CheckKetQuaVanHanhXoa_CreatorContent]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @CONTRACT_NUMBER NVARCHAR(100)
		, @CONTRACT_ID INT
		, @CONTRACT_DETAIL_ID INT
		, @AppKetQuaVanHanh_CreatorContent_ID INT
		, @ISDELETED SMALLINT
		, @GhiChu_DoiTruThucChay NVARCHAR(500) = N''
		, @Ghichu_TinhLaiThucChay NVARCHAR(500) = N''
		, @NgayGioiHanTinh_HDCT DATETIME = '2021-10-01'

	DECLARE @Table_ThucChay_CreatorContent TABLE
	(
		CONTRACT_ID int
		, CONTRACT_DETAIL_ID INT
		, AppKetQuaVanHanh_CreatorContent_ID INT
		, ISDELETED SMALLINT
	)
	--1. CHECK HOPDONGCHITET THAY DOI THANHTIEN VA BI XOA
	INSERT INTO @Table_ThucChay_CreatorContent
	(
		CONTRACT_ID 
		, CONTRACT_DETAIL_ID 
		, AppKetQuaVanHanh_CreatorContent_ID
		, ISDELETED 
	)
	--Check hop dong chi tiet thay doi
	--	Sản phẩm = Content Creator, ID=5184
	--- HTQC= Social Media, id=29
	SELECT 
    tc.HopDongBanREF,
    tc.PhanBoREF,
	tc.AppKetQuaVanHanh_CreatorContent_id,
    tc.IsDeleted
	FROM
	(
	SELECT * FROM dbo.AppKetQuaVanHanh_CreatorContent tc
	WHERE   TC.IsDeleted = 1 --XOA
			AND ISNULL(tc.PhanBoREF,0) <> 0
			AND tc.RecordStatus = 0
			AND tc.TrangThai in (3,5,6,7,8)
			AND ( CASE WHEN tc.CreationTime >= LastModificationTime THEN CONVERT(DATE, CreationTime)
						ELSE CONVERT(DATE, LastModificationTime)
					END ) = @NgayThucHien
	)tc INNER JOIN 
	(SELECT * FROM dbo.HopDong hd 
			WHERE hd.TrangThaiHopDong NOT IN (0,3)
			AND hd.NgayDanhSoHopDong >= @NgayGioiHanTinh_HDCT --pp mapping hdct tinh cho hd >=2021-10-01
	)hd ON tc.HopDongBanREF = hd.HopDongID

	DECLARE R_Cursor_KqvhCreatorContent CURSOR FOR 
	
	SELECT CONTRACT_ID 
		, CONTRACT_DETAIL_ID 
		, AppKetQuaVanHanh_CreatorContent_ID
		, ISDELETED 
	FROM @Table_ThucChay_CreatorContent
	ORDER BY CONTRACT_DETAIL_ID

	OPEN R_Cursor_KqvhCreatorContent

	-- Perform the first fetch.
	FETCH NEXT FROM R_Cursor_KqvhCreatorContent INTO  @CONTRACT_ID , @CONTRACT_DETAIL_ID , @AppKetQuaVanHanh_CreatorContent_ID
		, @ISDELETED 
			
	WHILE @@FETCH_STATUS = 0
	BEGIN
		DECLARE @ThucChayDaTinhID_output NVARCHAR(100) = ''
		SET @CONTRACT_NUMBER = ISNULL((SELECT TOP (1) hd.SoHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @CONTRACT_ID ORDER BY hd.HopDongID),'')
		--THUC HIEN DOI TRU TOAN BO ORDER NAY
		SET @GhiChu_DoiTruThucChay = ''
		--KET QUA VAN HANH BI XOA
		IF(@ISDELETED = 1)
		BEGIN
			--NEU TON TAI THUC CHAY VOI HOPDONGCHITIET
			IF(EXISTS(SELECT top (1) tcdt.HopDongChiTietREF, tcdt.DotChayBooking FROM DBO.ThucChayDaTinh tcdt
			WHERE tcdt.HopDongId = @CONTRACT_ID
			AND tcdt.HopDongChiTietREF = @CONTRACT_DETAIL_ID
			AND tcdt.DotChayBooking = @AppKetQuaVanHanh_CreatorContent_ID
			GROUP BY  tcdt.HopDongChiTietREF, tcdt.DotChayBooking HAVING SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiatriThayDoi) <> 0
			OR SUM(tcdt.ThanhTienKM + tcdt.GiatriKMThayDoi) <> 0 ))
			BEGIN
				--THUC HIEN DOI TRU TOAN BO
				SET @GhiChu_DoiTruThucChay = N'Doi Tru toan bo KQVH: ' + convert(nvarchar(100),@AppKetQuaVanHanh_CreatorContent_ID) + N' do kqvh CreatorContent bi huy'

				EXEC [dbo].[ThucChayDaTinh_DoiTru_ThanhTien_CreatorContent_ByKetQuaVanHanhID]
				@NgayGhiNhanThucChay				= @NgayThucHien,
				@HopDongREF							= @CONTRACT_ID,
				@HopDongChiTietREF					= @CONTRACT_DETAIL_ID,
				@AppKetQuaVanHanh_CreatorContent_id = @AppKetQuaVanHanh_CreatorContent_ID,
				@ghiChuDoiTru						= @GhiChu_DoiTruThucChay,
				@ThucChayDaTinhID_op				= @ThucChayDaTinhID_output OUTPUT
				
				
			END
		END
	

		FETCH NEXT FROM R_Cursor_KqvhCreatorContent INTO  @CONTRACT_ID , @CONTRACT_DETAIL_ID , @AppKetQuaVanHanh_CreatorContent_ID
		, @ISDELETED 
	END

	CLOSE R_Cursor_KqvhCreatorContent
	DEALLOCATE R_Cursor_KqvhCreatorContent



END

```
